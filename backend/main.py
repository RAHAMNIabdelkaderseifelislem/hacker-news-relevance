import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserBio(BaseModel):
    bio: str

HACKER_NEWS_API = "https://hacker-news.firebaseio.com/v0/"

def fetch_top_stories():
    response = requests.get(f"{HACKER_NEWS_API}topstories.json")
    top_story_ids = response.json()
    return top_story_ids[:500]  # Limit to top 500 stories

@app.post("/rank-stories")
async def rank_stories(user_bio: UserBio):
    top_story_ids = fetch_top_stories()
    # Placeholder for the actual implementation
    return {"message": "Ranking stories based on user bio", "top_story_ids": top_story_ids}
