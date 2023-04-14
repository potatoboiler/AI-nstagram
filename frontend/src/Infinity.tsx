import React, { useState, useCallback } from "react";
import InfiniteScroll from "react-infinite-scroller";
import Post from "./Post";

const makePost = (id: number) => <Post key={id} />;

function Infinity() {
  const [posts, setPosts]: [Array<Post>, any] = useState([]);
  const [fetching, setFetching] = useState(false);

  const loadFunc = useCallback(
    (page: number) => {
      if (fetching) return;
      setFetching(true);

      console.log(page);
      try {
        setPosts([...posts, makePost(posts.length)]);
      } finally {
        setFetching(false);
      }
    },
    [posts, fetching]
  );

  return (
    <InfiniteScroll loadMore={loadFunc} hasMore={true} loader={<>"TODO!"</>}>
      <>{posts}</>
    </InfiniteScroll>
  );
}

export default Infinity;
