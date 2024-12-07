import requests
import spacy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class UserBio(BaseModel):
    bio: str

HACKER_NEWS_API = "https://hacker-news.firebaseio.com/v0/"

# Check if the model is already downloaded, if not, download it
try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("Model 'en_core_web_sm' is already downloaded.")
except OSError:
    logger.info("Model 'en_core_web_sm' is not downloaded. Downloading now...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def fetch_top_stories() -> List[int]:
    response = requests.get(f"{HACKER_NEWS_API}topstories.json")
    top_story_ids = response.json()
    return top_story_ids[:500]  # Limit to top 500 stories

def fetch_story_details(story_id: int) -> dict:
    response = requests.get(f"{HACKER_NEWS_API}item/{story_id}.json")
    return response.json()

def rank_stories_by_relevance(user_bio: str, top_story_ids: List[int]) -> List[Tuple[int, int]]:
    user_keywords = [token.text.lower() for token in nlp(user_bio) if token.is_alpha]
    ranked_stories = []

    for story_id in top_story_ids:
        story_details = fetch_story_details(story_id)
        story_text = f"{story_details.get('title', '')} {story_details.get('text', '')}".lower()
        story_keywords = [token.text for token in nlp(story_text) if token.is_alpha]
        relevance_score = sum(keyword in story_keywords for keyword in user_keywords)
        ranked_stories.append((story_id, relevance_score))

    ranked_stories.sort(key=lambda x: x[1], reverse=True)
    return ranked_stories

@app.post("/rank-stories")
async def rank_stories(user_bio: UserBio):
    logger.info("Received bio: %s", user_bio.bio)
    top_story_ids = fetch_top_stories()
    ranked_stories = rank_stories_by_relevance(user_bio.bio, top_story_ids)
    logger.info("Ranked stories: %s", ranked_stories)
    return {"ranked_stories": ranked_stories}
