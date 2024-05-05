document.addEventListener("DOMContentLoaded", function () {
   const form = document.getElementById('answerForm');
   const goButton = document.getElementById('goButton');
   const submitButton = document.getElementById('submitButton');
   const textInput = document.getElementById('answerTextArea');


   form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission

      const formData = new FormData(form);
      const xhr = new XMLHttpRequest();

      xhr.open('POST', form.action, true);
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Add this header to identify AJAX requests

      xhr.onload = function () {
         if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            if (response.answer_status === 'correct') {
               // Update UI to indicate correct answer
               document.getElementById('answerTextArea').classList.add('border-success');
               submitButton.classList.add('d-none'); // Hide submit button
               document.getElementById('goButton').style.display = 'inline-block'; /* Show the 'GO' button */
            } else {
               // Update UI to indicate incorrect answer
               document.getElementById('answerTextArea').classList.add('border-danger');
               submitButton.classList.add('d-none'); // Hide submit button
               document.getElementById('goButton').style.display = 'inline-block'; /* Show the 'GO' button */
            }
            // Disable the textarea
            textInput.disabled = true;
         } else {
            console.error('Error submitting form');
         }
      };

      xhr.send(formData);
   });
});