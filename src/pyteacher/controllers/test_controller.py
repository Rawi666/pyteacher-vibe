"""
TestController for Strict Dictionary Test logic
"""
from typing import List, Optional
import random
from ..models.question import QuestionAnswer
from ..models.session import QuizSession
from ..utils.answer_validator import AnswerValidator


class QuizTestController:
    def __init__(self, questions: List[QuestionAnswer]):
        self.session = QuizSession(questions)
        self.asked = set()
        self.current_idx: Optional[int] = None
        self.question_order: List[int] = []
        self.current_position = 0

    def start_test(self):
        """Initialize test with randomized question order"""
        self.question_order = list(range(len(self.session.questions)))
        random.shuffle(self.question_order)
        self.current_position = 0
        self.current_idx = self._get_next_question_idx()

    def check_answer(self, user_input: str) -> bool:
        """Check if user answer is correct"""
        if self.current_idx is None:
            return False

        # Validate input first
        is_valid, _ = AnswerValidator.validate_input(user_input)
        if not is_valid:
            return False

        correct_answer = self.session.questions[self.current_idx].answer
        self.asked.add(self.current_idx)

        is_correct = AnswerValidator.compare_answers(user_input, correct_answer)

        if is_correct:
            self.session.mark_correct(self.current_idx)

        return is_correct

    def next_question(self):
        """Move to next question (each question asked only once)"""
        self.current_idx = self._get_next_question_idx()

    def get_current_correct_answer(self) -> str:
        """Get the correct answer for current question"""
        if self.current_idx is None:
            return ""
        return self.session.questions[self.current_idx].answer

    def update_statistics(self) -> dict:
        """Get current session statistics with test-specific labels"""
        stats = self.session.get_stats()
        # In test mode, we track correctly answered vs total asked
        stats['answered'] = len(self.asked)
        stats['left'] = len(self.session.questions) - len(self.asked)
        return stats

    def _get_next_question_idx(self) -> Optional[int]:
        """Get next question index (sequential through randomized order)"""
        if self.current_position >= len(self.question_order):
            return None  # All questions have been asked

        next_idx = self.question_order[self.current_position]
        self.current_position += 1
        return next_idx
