// main.js

// Wait for the document to be ready
document.addEventListener('DOMContentLoaded', function () {
    // Example: Add a click event listener to a button
    const myButton = document.getElementById('my-button');
    if (myButton) {
        myButton.addEventListener('click', function () {
            alert('Button Clicked!');
        });
    }

    // Example: Handle laptop comparison
    const compareButtons = document.querySelectorAll('.compare-btn');

    // Add a click event listener to each Compare button
    compareButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Get the laptop ID from a data attribute or URL
            const laptopId = button.dataset.laptopId;

            // Perform actions based on the laptop ID
            // For example, add the selected laptop to a comparison list
            addToComparisonList(laptopId);

            // Redirect to the comparison page
            window.location.href = '/compare/'; // Replace with your comparison page URL
        });
    });

    // Function to add a laptop to the comparison list
    function addToComparisonList(laptopId) {
        // Implement your logic to manage the comparison list here
        // You can use cookies, local storage, or a server-side approach to store the selected laptops.
    }

    // Example: Clear comparison list
    const clearComparisonButton = document.getElementById('clear-comparison');
    if (clearComparisonButton) {
        clearComparisonButton.addEventListener('click', function () {
            // Implement logic to clear the comparison list
            // This can be done using cookies, local storage, or a server-side approach.
        });
    }
});
