document.addEventListener('DOMContentLoaded', function() {
    // Function to add a laptop to the comparison list
    function addToCompare(laptopId) {
        // Logic to add laptop ID to comparison list
        // This might involve storing the ID in local storage or a global variable
    }

    // Function to update the comparison view
    function updateComparisonView() {
        // Fetch the details of laptops to be compared
        // This could be from local storage, a global variable, or an API call

        // Update the DOM to reflect the comparison list
        // This might involve dynamically creating a table or list in your HTML
    }

    // Event listener for 'Compare' buttons
    const compareButtons = document.querySelectorAll('.compare-button');
    compareButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            addToCompare(laptopId);
            updateComparisonView();
        });
    });

    // Optionally, event listeners for removing items from the comparison list

    // Function to clear the comparison list
    function clearComparison() {
        // Clear the comparison list from storage or variable
        // Update the comparison view
    }

    // Event listener for 'Clear Comparison' button
    const clearButton = document.querySelector('#clear-comparison');
    if (clearButton) {
        clearButton.addEventListener('click', function(event) {
            clearComparison();
        });
    }
});
