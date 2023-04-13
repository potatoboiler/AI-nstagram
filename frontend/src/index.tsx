import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Post from './Post';

const posts = ReactDOM.createRoot(
  document.getElementById('posts') as HTMLElement
);
posts.render(
  <>
    <Post />
    <Post />
    <Post />
  </>
);