import json

from question_model import Question
from quiz_brain import QuizBrain
from data_reader import DataProcessor

def pretty_print() -> None:
    print("\n")
    print("*"*100)

with open("data.json","r") as file:
    data = json.load(file)
dp = DataProcessor(data)
categories = dp.get_category_names()

# print(question_bank)
category_input_string = ""
for i,c in enumerate(categories):
    category_input_string += f"{i+1}. {c} \n"

pretty_print()
print("Welcome to the quiz game!")
print("Select the category.")
category = categories[int(input(category_input_string))-1]
pretty_print()

question_category = dp.get_category(category)
quiz_brain = QuizBrain(question_category)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
    pretty_print()

print("You've completed the quiz")
print(f"Your final score is: {quiz_brain.score}/{len(quiz_brain.question_list)}")
pretty_print()