from question_model import Question,QuestionCategory

class QuizBrain:
    def __init__(self,question_category: QuestionCategory) -> None:
        self.question_number = 0
        self.question_list = question_category.questions
        self.score = 0

    def next_question(self) -> None:
        question = self.question_list[self.question_number]
        print(f"Difficulty: {question.difficulty.title()}")
        self.increase_question_number()
        option_text, answer = self.random_option_generator(question)
        print(f"Q.{self.question_number} {question.question}: ")
        user_answer = int(input(option_text))

        self.check_answer(user_answer, answer, question.correct_answer)
        
    
    def increase_question_number(self) -> None:
        self.question_number += 1

    def still_has_question(self) -> bool:
        return len(self.question_list) > self.question_number
    
    def check_answer(self, user_answer: int, answer: int, correct_answer: str) -> None:
        if user_answer == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer is: {answer}.{correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        


    def random_option_generator(self, question: Question) -> tuple:
        import random
        options_input_string = ""
        random.shuffle(question.options)
        for i,o in enumerate(question.options):
            options_input_string += f"{i+1}. {o} \n"
        return options_input_string, question.options.index(question.correct_answer)+1

    