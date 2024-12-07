# Hacker News Relevance API

This project builds an API that ranks the top 500 stories from the Hacker News front page based on the relevance to a user-submitted bio.

## Architecture

### Backend
- **Framework:** FastAPI
- **Libraries:** requests, spacy
- **Deployment:** Render

### Frontend
- **Framework:** React
- **Libraries:** Tailwind CSS
- **Deployment:** Vercel

## Setup

### Backend
1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn main:app --reload`

### Frontend
1. Navigate to the `frontend` directory.
2. Install dependencies: `npm install`
3. Run the development server: `npm start`

## Deployment
- **Backend:** Deploy on Render.
- **Frontend:** Deploy on Vercel.
