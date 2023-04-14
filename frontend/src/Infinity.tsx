import React, { useState, useCallback } from "react";
import InfiniteScroll from "react-infinite-scroller";
import Post from "./Post";

function Infinity() {
  const [posts, setPosts]: [Array<typeof Post>, CallableFunction] = useState(
    []
  );
  const [fetching, setFetching] = useState(false);

  const loadFunc = useCallback(
    (page: number) => {
      if (fetching) return;
      setFetching(true);

      console.log(page);
      try {
        setPosts([...posts, <Post />]);
      } finally {
        setFetching(false);
      }
    },
    [posts, fetching]
  );

  return (
    <InfiniteScroll
      loadMore={loadFunc}
      hasMore={true}
      loader={<>"TODO!"</>}
      className="posts"
    >
      <>{posts}</>
    </InfiniteScroll>
  );
}

export default Infinity;
