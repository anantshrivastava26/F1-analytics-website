document.addEventListener('DOMContentLoaded', function() {
    window.submitForm = function(analysisType) {
        const analysisInput = document.getElementById('analysis_type');
        const raceSelection = document.getElementById('race_selection').value;
        
        analysisInput.value = analysisType;

        // Ensure the form gets submitted with race selection and analysis type
        document.getElementById('analysisForm').submit();
    };
});
