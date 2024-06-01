
async function createUser() {
    const data = {
        username: 'new_user',
        email: 'new_user@example.com',
        password: 'new_password'
    };
    try {
        const response = await fetch('/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error('Failed to create user');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function getUser(userId) {
    try {
        const response = await fetch(`/users/${userId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch user');
        }
        const user = await response.json();
        console.log(user);
    } catch (error) {
        console.error(error);
    }
}

async function updateUser(userId) {
    const data = {
        username: 'updated_user',
        email: 'updated_user@example.com',
        password: 'updated_password'
    };
    try {
        const response = await fetch(`/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) {
            throw new Error('Failed to update user');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function deleteUser(userId) {
    try {
        const response = await fetch(`/users/${userId}`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            throw new Error('Failed to delete user');
        }
        const responseData = await response.json();
        console.log(responseData);
    } catch (error) {
        console.error(error);
    }
}

async function fetchAndDisplayUsers() {
    try {
        const response = await fetch('/users/');
        if (!response.ok) {
            throw new Error('Failed to fetch users');
        }
        const users = await response.json();
        const usersContainer = document.getElementById('users-list');
        usersContainer.innerHTML = ''; // Clear previous users
        users.forEach(user => {
            const userElement = document.createElement('li');
            userElement.innerHTML = `
                <img src="static/dist/img/user3-128x128.jpg" alt="User Image"/> <!-- Update with actual image path -->
                <a class="users-list-name" href="#">${user.username}</a>
                <span class="users-list-date">${user.email}</span>
            `;
            usersContainer.appendChild(userElement);
        });
    } catch (error) {
        console.error('Error fetching users:', error.message);
    }
}

// Call the function to fetch and display users when the page loads
document.addEventListener('DOMContentLoaded', fetchAndDisplayUsers);


// Call the function to fetch and display users when the page loads
fetchAndDisplayUsers();

