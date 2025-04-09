
function BlogPost({post}) {
    return (
        <div className="post">
            <h5>{post.title}</h5>
            <p>{post.content}</p>
            <em>Written by {post.author}</em>
        </div>
    )
};

export default BlogPost;