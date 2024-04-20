from flask import Flask, render_template, Response, request, redirect, url_for, jsonify

pattern_questions = {

    "1": {
        "id": "1",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Tented Arch", "Central Pocket Whorl"]
    },
    "2": {
        "id": "2",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Arch", "Tented Arch", "Plain Loop"]
    },
    "3": {
        "id": "3",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Accidental Whorl", "Double Loop", "Central Pocket Whorl"]
    },
    "4": {
        "id": "4",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Central Pocket Whorl", "Accidental Whorl"]
    },
    "5": {
        "id": "5",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Arch", "Plain Loop", "Plain Whorl"]
    },
    "6": {
        "id": "6",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Central Pocket Whorl", "Double Loop"]
    },
    "7": {
        "id": "7",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "options": ["Plain Whorl", "Plain Loop", "Central Pocket Whorl"]
    }

}

minutiae_questions = {

    "1": {
        "id": "1",
        "image": "https://www.google.com",
        "question": "How many bifurcations are in the bottom right quadrant of this fingerprint?",
        "options": ["2", "5", "3"]
    },
    "2": {
        "id": "2",
        "image": "https://www.google.com",
        "question": "Name all minutiae present in top left corner of this fingerprint.",
        "answers": ["Bifurcation", "Ridge Ending", "Island"]
    },
    "3": {
        "id": "3",
        "image": "https://www.google.com",
        "question": "Label all letters with the appropriate minutiae.",
        "A": "Ridge Ending",
        "B": "Island",
        "C": "Spur",
        "D": "Bifurcation",
        "E": "Island",
        "F": "Bifurcation",
        "G": "Spur"
    },
    "4": {
        "id": "4",
        "image": "https://www.google.com",
        "question": "What pattern is this?",
        "single_answer": "spur"
    }

}

pattern_answers = [0, 0, 0, 0, 0, 0, 0] # 0 = incorrect, 1 = correct

minutiae_answers = [0, 0, 0, 0] # 0 = incorrect, 1 = correct



app = Flask(__name__)

@app.route('/quiz_pattern/<question_num>')
def quiz(question_num):
    pattern_question = pattern_questions[str(question_num)]
    return render_template('quiz_pattern.html', quiz_question=pattern_question)

#ADD POST INFORMATION TO RECEIVE WHETHER THE ANSWER IS CORRECT OR NOT

@app.route('/quiz_minutiae/<question_num>')
def quiz(question_num):
    minutiae_question = minutiae_questions[str(question_num)]
    return render_template('quiz_minutiae.html', quiz_question=minutiae_question)

@app.route('/quiz_pattern/results')
def quiz_results():
    quiz_results = sum(pattern_answers)
    return render_template('quiz_results.html', quiz_results=quiz_results)