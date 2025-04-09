import "./BlogPost"
import BlogPost from "./BlogPost";

function BlogList({posts}) {
    return (
        <div className="blog-posts">
            { posts.map(post => (
                <BlogPost key={post.id} post={post} />
            ))}
        </div>
    )
};

export default BlogList;