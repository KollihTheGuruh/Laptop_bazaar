document.addEventListener('DOMContentLoaded', function() {
    // Initialize an array to store laptop IDs for comparison
    let comparisonList = [];

    // Function to add a laptop to the comparison list
    function addToCompare(laptopId) {
        // Check if the laptopId is not already in the comparisonList
        if (!comparisonList.includes(laptopId)) {
            comparisonList.push(laptopId);
            // Optionally, you can store the comparisonList in local storage for persistence
            localStorage.setItem('comparisonList', JSON.stringify(comparisonList));
        }
    }

    // Function to remove a laptop from the comparison list
    function removeFromCompare(laptopId) {
        const index = comparisonList.indexOf(laptopId);
        if (index !== -1) {
            comparisonList.splice(index, 1);
            // Update local storage if you're using it
            localStorage.setItem('comparisonList', JSON.stringify(comparisonList));
        }
    }

    // Function to update the comparison view
    function updateComparisonView() {
        // Fetch the details of laptops to be compared using comparisonList
        // You can make an API call to get laptop details based on the IDs in comparisonList

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

    // Event listener for 'Remove' buttons (for removing laptops from comparison)
    const removeButtons = document.querySelectorAll('.remove-button');
    removeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            removeFromCompare(laptopId);
            updateComparisonView();
        });
    });

    // Function to clear the comparison list
    function clearComparison() {
        // Clear the comparisonList array
        comparisonList = [];
        // Optionally, remove the comparisonList from local storage
        localStorage.removeItem('comparisonList');
        // Update the comparison view
        updateComparisonView();
    }

    // Event listener for 'Clear Comparison' button
    const clearButton = document.querySelector('#clear-comparison');
    if (clearButton) {
        clearButton.addEventListener('click', function(event) {
            clearComparison();
        });
    }

    // Optionally, check for a stored comparisonList in local storage and initialize it
    const storedComparisonList = localStorage.getItem('comparisonList');
    if (storedComparisonList) {
        comparisonList = JSON.parse(storedComparisonList);
        updateComparisonView();
    }
});
