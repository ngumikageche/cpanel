
async function createBlog() {
    const data = {
        title: 'New Blog Post Title',
        content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        user_id: 1 // Replace with the appropriate user ID
    };
    try {
        const response = await fetch('/blogs/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error('Failed to create blog post');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function getBlog(blogId) {
    try {
        const response = await fetch(`/blogs/${blogId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch blog');
        }
        const blog = await response.json();
        console.log(blog);
    } catch (error) {
        console.error(error);
    }
}

async function updateBlog(blogId) {
    const data = {
        title: 'Updated Blog Post Title',
        content: 'Updated content goes here'
    };
    try {
        const response = await fetch(`/blogs/${blogId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error('Failed to update blog post');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function deleteBlog(blogId) {
    try {
        const response = await fetch(`/blogs/${blogId}`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            throw new Error('Failed to delete blog post');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function fetchAndDisplayBlogs() {
    try {
        const response = await fetch('/blogs/');
        if (!response.ok) {
            throw new Error('Failed to fetch blogs');
        }
        const blogs = await response.json();
        const blogsContainer = document.getElementById('blogs-container');
        blogsContainer.innerHTML = ''; // Clear previous blogs
        blogs.forEach(blog => {
            const blogElement = document.createElement('div');
            blogElement.innerHTML = `
                <h2>${blog.title}</h2>
                <p>${blog.content}</p>
                <p>Author ID: ${blog.user_id}</p>
                <p>Created At: ${blog.created_at}</p>
                <p>Updated At: ${blog.updated_at}</p>
                <hr>
            `;
            blogsContainer.appendChild(blogElement);
        });
    } catch (error) {
        console.error(error);
    }
}

// Call the function to fetch and display blogs when the page loads
fetchAndDisplayBlogs();
