class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("Well done! 😘😘 that is correct!!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("Sorry, that's wrong 😒")
            print(f"Your score is {self.score}/{self.question_number}")

    def next_question(self):

            user_answer = input(f"Q.{self.question_number + 1}: "
                             f"{self.question_list[self.question_number].text} (True/False)?: ")

            self.question_number += 1
            correct_answer = self.question_list[self.question_number].answer
            self.check_answer(user_answer, correct_answer)




