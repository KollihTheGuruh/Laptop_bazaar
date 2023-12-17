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
            updateComparisonView();
        }
    }

    // Function to remove a laptop from the comparison list
    function removeFromCompare(laptopId) {
        const index = comparisonList.indexOf(laptopId);
        if (index !== -1) {
            comparisonList.splice(index, 1);
            // Update local storage if you're using it
            localStorage.setItem('comparisonList', JSON.stringify(comparisonList));
            updateComparisonView();
        }
    }

    // Function to update the comparison view
    function updateComparisonView() {
        console.log('Updating comparison view...');
        // Fetch the details of laptops to be compared using comparisonList
        // You can make an API call to get laptop details based on the IDs in comparisonList

        // Update the DOM to reflect the comparison list
        // This might involve dynamically creating a table or list in your HTML
        const comparisonContainer = document.querySelector('.compare-container');
        if (comparisonContainer) {
            if (comparisonList.length > 0) {
                comparisonContainer.innerHTML = '<p>Comparing Laptops:</p>';
                comparisonList.forEach(laptopId => {
                    // Fetch laptop details based on ID and update the DOM
                    comparisonContainer.innerHTML += `<p>Laptop ID: ${laptopId}</p>`;
                });
                // Optionally, you can add a button or link to navigate to the compare page
                comparisonContainer.innerHTML += `<a href="{% url 'compare_view' %}?laptop_ids=${comparisonList.join(',')}" class="btn compare-btn">Compare Now</a>`;
            } else {
                comparisonContainer.innerHTML = '<p>Please select laptops to compare.</p>';
            }
        }
    }

    // Event listener for 'Compare' buttons
    const compareButtons = document.querySelectorAll('.compare-button');
    compareButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            addToCompare(laptopId);
        });
    });

    // Event listener for 'Remove' buttons (for removing laptops from comparison)
    const removeButtons = document.querySelectorAll('.remove-button');
    removeButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            removeFromCompare(laptopId);
        });
    });

    // Function to clear the comparison list
    function clearComparison() {
        console.log('Clearing comparison...');
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
