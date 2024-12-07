import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [bio, setBio] = useState('');
  const [stories, setStories] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/rank-stories', { bio });
      setStories(response.data.ranked_stories);
    } catch (error) {
      console.error('Error ranking stories:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Hacker News Relevance Ranker</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          className="w-full h-32 p-2 border rounded mb-4"
          value={bio}
          onChange={(e) => setBio(e.target.value)}
          placeholder="Enter your bio..."
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Submit</button>
      </form>
      <div className="mt-4">
        <h2 className="text-xl font-bold mb-2">Ranked Stories</h2>
        <ul>
          {stories.map((story, index) => (
            <li key={index} className="mb-2">
              <a href={`https://news.ycombinator.com/item?id=${story[0]}`} target="_blank" rel="noopener noreferrer" className="text-blue-500">
                Story {index + 1} (Score: {story[1]})
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
