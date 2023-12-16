document.addEventListener('DOMContentLoaded', function() {
    let comparisonArray = [];

    function addToCompare(laptopId) {
        if (!comparisonArray.includes(laptopId) && comparisonArray.length < 6) {
            comparisonArray.push(laptopId);
            console.log('Added to compare:', laptopId); // Debug log
        }
        updateComparisonView();
    }

    function removeFromCompare(laptopId) {
        comparisonArray = comparisonArray.filter(id => id !== laptopId);
        console.log('Removed from compare:', laptopId); // Debug log
        updateComparisonView();
    }

    function updateComparisonView() {
        const comparisonCount = document.querySelector('#comparison-count');
        if (comparisonCount) {
            comparisonCount.textContent = `Compare (${comparisonArray.length})`;
        }

        const compareButton = document.querySelector('#compare-button');
        if (compareButton) {
            compareButton.disabled = comparisonArray.length < 2 || comparisonArray.length > 6;
        }

        console.log('Current comparison array:', comparisonArray); // Debug log
    }

    document.querySelectorAll('.compare-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            addToCompare(laptopId);
        });
    });

    document.querySelectorAll('.remove-button').forEach(button => {
        button.addEventListener('click', function(event) {
            const laptopId = this.dataset.laptopId;
            removeFromCompare(laptopId);
        });
    });

    function navigateToComparisonPage() {
        window.location.href = `/compare?laptops=${comparisonArray.join(',')}`;
    }

    const compareNowButton = document.querySelector('#compare-button');
    if (compareNowButton) {
        compareNowButton.addEventListener('click', function(event) {
            if (comparisonArray.length >= 2 && comparisonArray.length <= 6) {
                navigateToComparisonPage();
            } else {
                alert('Please select between 2 to 6 laptops for comparison.'); // User feedback
            }
        });
    }

    function clearComparison() {
        comparisonArray = [];
        updateComparisonView();
    }

    const clearButton = document.querySelector('#clear-comparison');
    if (clearButton) {
        clearButton.addEventListener('click', function(event) {
            clearComparison();
        });
    }
});
