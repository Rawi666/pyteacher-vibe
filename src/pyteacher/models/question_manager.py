"""
QuestionManager for managing questions and session statistics
"""
from typing import List, Dict
from .question import QuestionAnswer

class QuestionManager:
    def __init__(self, questions: List[QuestionAnswer]):
        self.questions = questions
        self.correct = set()
        self.asked = set()

    def get_random_question(self) -> QuestionAnswer:
        import random
        idx = random.choice([i for i in range(len(self.questions)) if i not in self.correct])
        self.asked.add(idx)
        return self.questions[idx]

    def mark_question_correct(self, question_id: int):
        self.correct.add(question_id)

    def get_session_statistics(self) -> Dict[str, int]:
        return {
            "total": len(self.questions),
            "learned": len(self.correct),
            "left": len(self.questions) - len(self.correct)
        }
