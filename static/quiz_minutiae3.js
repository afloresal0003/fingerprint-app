document.addEventListener("DOMContentLoaded", function () {
   const form = document.getElementById('answerForm');
   const goButton = document.getElementById('goButton');
   const submitButton = document.getElementById('submitButton');
   const answerInputs = document.querySelectorAll('.form-control');
   console.log(answerInputs)

   form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent the default form submission

      const formData = new FormData(form);

      const xhr = new XMLHttpRequest();
      xhr.open('POST', form.action, true);
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); // Add this header to identify AJAX requests

      xhr.onload = function () {
         if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const answerStatus = response.answer_status;

            // Update UI based on correctness of each input
            for (let i = 0; i < answerInputs.length; i++) {
               const input = answerInputs[i];
               const letter = String.fromCharCode(65 + i); // A=65, B=66, ..., G=71

               if (answerStatus[letter] === 'correct') {
                  input.classList.add('border-success');
               } else {
                  input.classList.add('border-danger');
               }
            }

            // Hide submit button and show 'GO' button
            submitButton.classList.add('d-none');
            goButton.style.display = 'inline-block';
            // Disable all text inputs
            answerInputs.forEach(function (input) {
               input.disabled = true;
            });
         } else {
            console.error('Error submitting form');
         }
      };

      xhr.send(formData);
   });
});
