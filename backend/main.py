import requests
import spacy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserBio(BaseModel):
    bio: str

HACKER_NEWS_API = "https://hacker-news.firebaseio.com/v0/"
nlp = spacy.load("en_core_web_sm")

def fetch_top_stories():
    response = requests.get(f"{HACKER_NEWS_API}topstories.json")
    top_story_ids = response.json()
    return top_story_ids[:500]  # Limit to top 500 stories

def fetch_story_details(story_id):
    response = requests.get(f"{HACKER_NEWS_API}item/{story_id}.json")
    return response.json()

def rank_stories_by_relevance(user_bio, top_story_ids):
    user_keywords = [token.text for token in nlp(user_bio) if token.is_alpha]
    ranked_stories = []

    for story_id in top_story_ids:
        story_details = fetch_story_details(story_id)
        story_text = f"{story_details.get('title', '')} {story_details.get('text', '')}"
        story_keywords = [token.text for token in nlp(story_text) if token.is_alpha]
        relevance_score = sum(keyword in story_keywords for keyword in user_keywords)
        ranked_stories.append((story_id, relevance_score))

    ranked_stories.sort(key=lambda x: x[1], reverse=True)
    return ranked_stories

@app.post("/rank-stories")
async def rank_stories(user_bio: UserBio):
    top_story_ids = fetch_top_stories()
    ranked_stories = rank_stories_by_relevance(user_bio.bio, top_story_ids)
    return {"ranked_stories": ranked_stories}
