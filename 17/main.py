"""Main file for question program"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

# for question in question_bank:
#     print(f"{question.text} ? {question.answer}")

quiz = QuizBrain(question_bank)
quiz.next_question()
