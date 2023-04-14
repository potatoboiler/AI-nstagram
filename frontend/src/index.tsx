import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Post from './Post';
import Infinity from './Infinity';

const posts = ReactDOM.createRoot(
  document.getElementById('posts') as HTMLElement
);
posts.render(
  <>
    <Infinity />
  </>
);