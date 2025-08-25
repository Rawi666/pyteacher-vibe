"""
QuizSession class for managing session state
"""
from typing import List
from .question import QuestionAnswer

class QuizSession:
    def __init__(self, questions: List[QuestionAnswer]):
        self.questions = questions
        self.correct = set()
        self.asked = set()

    def mark_correct(self, idx: int):
        self.correct.add(idx)

    def mark_asked(self, idx: int):
        self.asked.add(idx)

    def get_stats(self):
        return {
            "total": len(self.questions),
            "learned": len(self.correct),
            "left": len(self.questions) - len(self.correct)
        }
