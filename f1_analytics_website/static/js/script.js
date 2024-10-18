document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is loaded and ready.");

    // Function to handle card clicks and submit form
    window.submitForm = function(analysisType) {
        const analysisInput = document.getElementById('analysis_type');
        analysisInput.value = analysisType;
        document.getElementById('analysisForm').submit();
    };
});