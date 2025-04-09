import BlogList from "./BlogList";

function BlogCategory ({ category, posts }) {
    return (
        <div>
			<h3>{ category }</h3>
            <hr />
			<BlogList posts={ posts } />
		</div>
    )
}

export default BlogCategory;