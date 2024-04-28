// function handleButtonClick(button) {
//    var buttons = document.getElementsByClassName('custom-button');
//    for (var i = 0; i < buttons.length; i++) {
//       buttons[i].disabled = true; /* Disable all buttons after selection */
//    }
//    button.classList.add('selected'); /* Add 'selected' class to the clicked button */
//    document.getElementById('goButton').style.display = 'inline-block'; /* Show the 'GO' button */
   
// }

function handleButtonClick(button) {
   var buttons = document.getElementsByClassName('custom-button');
   for (var i = 0; i < buttons.length; i++) {
      buttons[i].disabled = true; /* Disable all buttons after selection */
   }
   button.classList.add('selected'); /* Add 'selected' class to the clicked button */

   // Check if the selected answer is correct
   var selectedAnswer = button.value;
   var correctAnswer = document.getElementById('answerDiv').getAttribute('questionAnswer'); /* Get the correct answer*/
   console.log("Selected Answer: " + selectedAnswer)
   console.log("Correct Answer: " + correctAnswer)
   if (selectedAnswer === correctAnswer) {
      button.classList.add('correct'); /* Add 'correct' class to the button */
      console.log("ANSWER IS CORRECT!")
   } else {
      console.log("ANSWER IS INCORRECT!")
      button.classList.add('incorrect'); /* Add 'incorrect' class to the button */
      // Find the button with the correct answer and add 'correct' class to it
      var options = document.getElementsByClassName('custom-button');
      for (var j = 0; j < options.length; j++) {
         if (options[j].value === correctAnswer) {
            options[j].classList.add('correct');
            break;
         }
      }
   }

   document.getElementById('goButton').style.display = 'inline-block'; /* Show the 'GO' button */
}