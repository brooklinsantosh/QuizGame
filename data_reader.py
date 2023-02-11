from question_model import Question, QuestionCategory, QuestionBank

class DataProcessor:
    def __init__(self, data: list[dict]) -> None:
        self.data = data
    def get_all(self) -> QuestionBank:
        question_bank_lst = []
        for d in self.data:
            question_category = QuestionCategory(
                category= d['category'],
                questions= [Question(q['type'],q['difficulty'],q['question'],q['correct_answer'],q['incorrect_answers']) for q in d['data']]
            )
            question_bank_lst.append(question_category)
        return QuestionBank(question_bank_lst)
    def get_category(self,category: str) -> QuestionCategory:
        for d in self.data:
            if d['category'] == category:
                question_category = QuestionCategory(
                    category= d['category'],
                    questions= [Question(q['type'],q['difficulty'],q['question'],q['correct_answer'],q['incorrect_answers']) for q in d['data']]
                )
        return question_category
    
    def get_category_names(self) -> list[str]:
        return [d['category'] for d in self.data]


