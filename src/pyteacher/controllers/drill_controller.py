"""
DrillController for Strict Dictionary Drill logic
"""
from typing import List
from ..models.question import QuestionAnswer
from ..models.session import QuizSession

class DrillController:
    def __init__(self, questions: List[QuestionAnswer]):
        self.session = QuizSession(questions)
        self.current_idx = None

    def start_drill(self):
        self.current_idx = self._get_next_question_idx()

    def check_answer(self, user_input: str) -> bool:
        if self.current_idx is None:
            return False
        correct = self.session.questions[self.current_idx].answer
        if user_input.strip().lower() == correct.strip().lower():
            self.session.mark_correct(self.current_idx)
            return True
        return False

    def next_question(self):
        self.current_idx = self._get_next_question_idx()

    def update_statistics(self):
        return self.session.get_stats()

    def _get_next_question_idx(self):
        for idx, q in enumerate(self.session.questions):
            if idx not in self.session.correct:
                return idx
        return None
