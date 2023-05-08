class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0


    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            print(f"\nWell Played.\nYour final score is {self.score}/12")
            print("Hope you enjoyed this quiz game!")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number} {current_question} (True/False): ")
        self.check_answer(user_answer, current_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry! You gave the wrong answer.")
            self.score -= 1
        print(f"The correct answer was: {correct_answer}")
        print(f"Your quiz score is {self.score}/{self.question_number}\n")