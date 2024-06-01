function validateAndCreateProduct() {
    var form = document.getElementById('productForm');

    // Check if the form is valid
    if (form.checkValidity()) {
        // If the form is valid, create the product
        createProduct();
    } else {
        // If the form is not valid, show the validation errors
        $(form).addClass('was-validated');
    }
}

function createProduct() {
    var form = document.getElementById('productForm');
    var formData = new FormData(form);

    $.ajax({
        url: 'products/product/create',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            toastr.success('Product created successfully! Product ID: ' + response.product_id);
            // Optionally, you can reset the form here
            form.reset();
            // Reload the page after a short delay (e.g., 1 second)
            setTimeout(function() {
                location.reload();
            }, 1000);
        },
        error: function(xhr, status, error) {
            console.log(xhr); // Log the entire xhr object to see its structure and contents
            var errorMessage = xhr.status + ': ' + xhr.statusText;
            toastr.error('Error - ' + errorMessage);
            // Reload the page after a short delay (e.g., 1 second)
            setTimeout(function() {
                location.reload();
            }, 1000);
        }
    });
}



// Fetch and display products
function displayProducts() {
    fetch('products') // Assuming this endpoint returns product data
        .then(response => response.json())
        .then(data => {
            const products = data.products;
            const tableBody = document.querySelector('#productTable tbody');
            tableBody.innerHTML = ''; // Clear existing table rows

            products.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.name}</td>
                    <td>${product.description}</td>
                    <td>${product.price}</td>
                    <td>${product.stock}</td>
                    <td>${product.category_id}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching products:', error);
        });
}

// Call the function to display products when the page loads
window.onload = displayProducts;
