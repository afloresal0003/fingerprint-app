$(document).ready(function() {

    var patternNum = 1; // Start with the first question
    loadQuestion(questionNum);

    $('#nextButton').click(function() {
        // You should have logic to determine when to stop navigating to next questions
        // For now, let's assume there are 3 questions
        if (patternNum < 7) {
            patternNum++;
            navigateToPatternQuizPage(patternNum);
        }
        else {
            navigateToResultsPage();
        }
    });

    function loadQuestion(questionNum) {
        $.ajax({
            url: '/quiz_pattern/' + questionNum,
            type: 'GET',
            success: function(response) {
                var quizQuestion = JSON.parse(response);
                $('#questionTitle').text('Question ' + questionNum);
                $('#questionInput').val(quiz_question.question);
                $('#questionImage').attr('src', quiz_question.image);
                $('#answers').empty();
                $.each(quizQuestion.answers, function(index, value) {
                    var button = $('<button>').addClass('btn btn-primary').text(value);
                    $('#answers').append($('<div>').addClass('col-md-4').append(button));
                });
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    }

    function navigateToPatternQuizPage(question_num) {
        var url = "/quiz_pattern/" + question_num;
        window.location.href = url;
    }
    
    function navigatetoMinutiaeQuizPage(question_num) {
        var url = "/quiz_minutiae/" + question_num;
        window.location.href = url;
    }

    function navigateToResultsPage(){
        var url = "/quiz_pattern/results";
    }

});