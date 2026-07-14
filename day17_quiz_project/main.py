from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(1, len(question_data)+1):
    q_i = Question(question_data[i-1]["text"], question_data[i-1]["answer"])
    question_bank.append(q_i)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


