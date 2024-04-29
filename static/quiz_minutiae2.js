document.addEventListener("DOMContentLoaded", function () {
   const form = document.getElementById('answerForm');
   const goButton = document.getElementById('goButton');
   const submitButton = document.getElementById('submitButton');
   const answerTextArea = document.getElementById('answerTextArea');

   form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission

      const answer = answerTextArea.value.trim(); // Get the user's input
      const answerList = answer.split(',').map(item => item.trim()); // Split the input into a list of answers

      // Check if the input is a valid comma-separated list with exactly 3 items
      if (answerList.length !== 3 || answerList.some(item => item === '')) {
         answerTextArea.classList.add('border-danger'); // Make the text area border red
         return; // Exit early if the input is not valid
      }

      const formData = new FormData(form);
      const xhr = new XMLHttpRequest();

      xhr.open('POST', form.action, true);
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Add this header to identify AJAX requests

      xhr.onload = function () {
         if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.answer_status === 'correct') {
               // Update UI to indicate correct answer
               answerTextArea.classList.add('border-success');
               submitButton.classList.add('d-none'); // Hide submit button
               goButton.style.display = 'inline-block'; // Show the 'GO' button
            } else {
               // Update UI to indicate incorrect answer
               answerTextArea.classList.add('border-danger');
               submitButton.classList.add('d-none'); // Hide submit button
               goButton.style.display = 'inline-block'; // Show the 'GO' button
            }
         } else {
            console.error('Error submitting form');
         }
      };

      xhr.send(formData);
   });
});
