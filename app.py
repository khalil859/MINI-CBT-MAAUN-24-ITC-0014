2.app.py 
from flask import Flask, render_template, request
from models import Question
from datetime import datetime

app = Flask(__name__)

# Questions (your data)
questions = [
    Question("What is the capital of Nigeria?", "Abuja"),
    Question("2 + 2 = ?", "4"),
    Question("Python is a programming language? (yes/no)", "yes")
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        if question.check_answer(user_answer):
            score += 1

    time_submitted = datetime.now()

    return render_template("result.html", score=score, total=len(questions), time=time_submitted)

if __name__ == "__main__":
    app.run(debug=True)