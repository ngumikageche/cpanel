function createCategory() {
    // Get the category name from the input field
    var categoryName = document.getElementById('categoryName').value;

    // Validate if category name is provided
    if (!categoryName) {
        alert('Please provide a category name');
        return;
    }

    // Prepare data to send to the server
    var formData = new FormData();
    formData.append('name', categoryName);

    // Send POST request to the server
    $.ajax({
        url: '/categories/create',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            toastr.success('Category created successfully! Category ID: ' + response.category_id);
            // Optionally, you can reset the form here
            form.reset();
        },
        error: function(xhr, status, error) {
            console.log(xhr); // Log the entire xhr object to see its structure and contents
            var errorMessage = xhr.status + ': ' + xhr.statusText;
            toastr.error('Error - ' + errorMessage);
        }
    });
}
// Function to display categories
function displayCategories() {
    fetch('/categories') // Assuming this endpoint returns category data
        .then(response => response.json())
        .then(categories => {
            console.log(categories); // Log the categories data
            console.log("done");
            const tableBody = document.querySelector('#categoryTable tbody');
            tableBody.innerHTML = ''; // Clear existing table rows

            categories.forEach(category => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${category.id}</td>
                    <td>${category.name}</td>
                    <td>
                        <button onclick="editCategory(${category.id})">Edit</button>
                        <button onclick="deleteCategory(${category.id})">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
}


// Function to call displayCategories() when the page loads
window.onload = displayCategories;

