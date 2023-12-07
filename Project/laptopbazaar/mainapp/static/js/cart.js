document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for Add to Cart buttons
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            addToCart(laptopId);
        });
    });

    // Function to add an item to the cart
    function addToCart(laptopId) {
        // Assuming you have an API endpoint to handle adding items to the cart
        fetch(`/api/add-to-cart/${laptopId}/`, {
            method: 'POST',
            // Additional configurations like headers, body, etc.
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                updateCartDisplay(); // Update your cart display here
            } else {
                console.error('Failed to add item to cart.');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Function to update cart display
    function updateCartDisplay() {
        // Fetch updated cart data and update the display
        // This could involve updating a cart icon, item count, etc.
    }

    // Additional functions for updating and removing items from the cart can be added similarly
});
