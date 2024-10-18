document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is loaded and ready.");

    // You can add any JavaScript logic here, for example, form validation.
    
    // Example: Simple form validation for analysis type selection
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const select = document.getElementById('analysis_type');
        if (select.value === '') {
            event.preventDefault();
            alert('Please select an analysis type before submitting.');
        }
    });
});
