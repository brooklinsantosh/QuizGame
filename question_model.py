from dataclasses import dataclass, field
from enum import StrEnum, auto

class QuestionType(StrEnum):
    BOOLEAN = auto()
    MULTIPLE = auto()

@dataclass
class Question:
    question_type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]
    options: list[str] = field(init=False)

    def __post_init__(self)-> None:
        self.options = [op for op in self.incorrect_answers+[self.correct_answer]]

@dataclass
class QuestionCategory:
    category: str
    questions: list[Question]

@dataclass
class QuestionBank:
    question_bank: list[QuestionCategory]


