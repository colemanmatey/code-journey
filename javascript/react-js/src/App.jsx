import './App.css'
import './components/BlogList'
import BlogList from './components/BlogList';
import BlogCategory from './components/BlogCategory';

function App() {

	const posts = [
		{id: 1, title: "The Secret to Productivity: 5 Easy Hacks", content: "Learn how to streamline your day with these proven techniques that boost efficiency and cut down on procrastination.", author: "Alex Johnson", genre: "Self-Help"},
		{id: 2, title: "Top 10 Travel Destinations for 2025", content: "From the serene beaches of Maldives to the bustling streets of Tokyo, discover this year's must-visit places.", author: "Emily Carter", genre: "Travel"},
		{id: 3, title: "The Future of AI: What's Next?", content: "Artificial Intelligence is evolving rapidly. Explore the latest trends and innovations in this exciting field.", author: "John Smith", genre: "Technology"},
		{id: 4, title: "Mastering Healthy Eating in a Busy World", content: "Tired of fast food? Here’s how you can prepare quick, nutritious meals without sacrificing your schedule.", author: "Rachel Green", genre: "Health & Wellness"},
		{id: 5, title: "Why Morning Routines Are Key to Success", content: "Early risers often have an edge. Find out how a well-crafted morning routine can set the tone for your day.", author: "Chris Anderson", genre: "Self-Help"},
		{id: 6, title: "Exploring the Benefits of Meditation", content: "Reduce stress and improve focus with meditation. We dive into techniques that beginners can use to get started.", author: "Sophia Lopez", genre: "Health & Wellness"},
		{id: 7, title: "The Evolution of Social Media Platforms", content: "From MySpace to TikTok, take a nostalgic journey through the rise of social media and its impact.", author: "David Brown", genre: "Technology"},
		{id: 8, title: "5 DIY Home Projects to Try This Weekend", content: "Transform your space with simple yet effective DIY projects that anyone can tackle.", author: "Linda Wilson", genre: "Lifestyle"},
		{id: 9, title: "How to Stay Fit While Working from Home", content: "Don't let your desk job take a toll on your health. These easy exercises will keep you active.", author: "Michael Taylor", genre: "Fitness"},
		{id: 10, title: "The Art of Negotiation: Skills for Everyday Life", content: "Negotiation isn't just for boardrooms. Learn how to apply these strategies in daily situations.", author: "Jessica Kim", genre: "Business"},
		{id: 11, title: "The Science Behind Good Sleep", content: "Dive into how sleep affects our body and learn tips to improve your nightly rest.", author: "Rachel Green", genre: "Health & Wellness"},
		{id: 12, title: "Sustainable Travel Tips", content: "Explore how to travel responsibly and minimize your environmental footprint.", author: "Emily Carter", genre: "Travel"},
		{id: 13, title: "The Rise of Electric Vehicles", content: "Electric cars are transforming the auto industry. Learn about the latest models and innovations.", author: "John Smith", genre: "Technology"},
		{id: 14, title: "Creative Writing: Tips for Beginners", content: "Unlock your creativity and learn how to craft compelling stories.", author: "Jessica Kim", genre: "Art & Writing"},
		{id: 15, title: "Quick Workouts for Busy Professionals", content: "Stay fit even with a packed schedule using these effective routines.", author: "Michael Taylor", genre: "Fitness"},
		{id: 16, title: "Gardening Hacks for Urban Spaces", content: "Learn how to turn small areas into thriving gardens with these tips.", author: "Linda Wilson", genre: "Lifestyle"},
		{id: 17, title: "Digital Privacy: Staying Safe Online", content: "Protect your data and stay secure while navigating the online world.", author: "David Brown", genre: "Technology"},
		{id: 18, title: "The Psychology of Motivation", content: "Discover how to tap into your internal drive and achieve your goals.", author: "Chris Anderson", genre: "Self-Help"},
		{id: 19, title: "The Perfect Weekend Getaway", content: "Ideas for short trips that will refresh and energize you.", author: "Emily Carter", genre: "Travel"},
		{id: 20, title: "Nutrition Myths Debunked", content: "Separate fact from fiction when it comes to healthy eating.", author: "Rachel Green", genre: "Health & Wellness"}
	];

	return (
		<div>
			<h1>Cole's blog</h1>

			<h3>All Posts</h3>
			<hr />
			<BlogList posts={posts} />


			<BlogCategory category='Self-Help' posts={posts.filter((post) => (post.genre === 'Self-Help'))} />
			<BlogCategory category='Travel' posts={posts.filter((post) => (post.genre === 'Travel'))} />
			<BlogCategory category='Technology' posts={posts.filter((post) => (post.genre === 'Technology'))} />
			<BlogCategory category='Health & Wellness' posts={posts.filter((post) => (post.genre === 'Health & Wellness'))} />
			<BlogCategory category='Lifestyle' posts={posts.filter((post) => (post.genre === 'Lifestyle'))} />
			<BlogCategory category='Fitness' posts={posts.filter((post) => (post.genre === 'Fitness'))} />
			<BlogCategory category='Business' posts={posts.filter((post) => (post.genre === 'Business'))} />
			<BlogCategory category='Art & Writing' posts={posts.filter((post) => (post.genre === 'Art & Writing'))} />
		</div>
	)
}

export default App;
