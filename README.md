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

## Thought Process and Decisions

### Backend
- **FastAPI:** Chosen for its simplicity and performance. It allows for quick development and easy deployment.
- **requests:** Used for making API calls to the Hacker News API.
- **spacy:** Chosen for its powerful NLP capabilities, making it easy to process and analyze text.

### Frontend
- **React:** Chosen for its component-based architecture and ease of use.
- **Tailwind CSS:** Chosen for its utility-first CSS framework, allowing for quick and responsive styling.

### Deployment
- **Render:** Chosen for its ease of use and quick deployment for the backend.
- **Vercel:** Chosen for its seamless integration with React and quick deployment for the frontend.

### Optimizations
- Limited the number of top stories to 500 to optimize performance.
- Used basic keyword matching for relevance ranking to keep the implementation simple and quick.
