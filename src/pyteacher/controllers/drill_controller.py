"""
DrillController for Strict Dictionary Drill logic
"""
from typing import List, Optional
import random
from ..models.question import QuestionAnswer
from ..models.session import QuizSession
from ..utils.answer_validator import AnswerValidator


class DrillController:
    def __init__(self, questions: List[QuestionAnswer]):
        self.session = QuizSession(questions)
        self.current_idx: Optional[int] = None
        self.question_order: List[int] = []
        self.current_position = 0

    def start_drill(self):
        """Initialize the drill with randomized question order"""
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
        is_correct = AnswerValidator.compare_answers(user_input, correct_answer)

        if is_correct:
            self.session.mark_correct(self.current_idx)

        return is_correct

    def next_question(self):
        """Move to next question according to drill logic"""
        if self.current_idx is None:
            return

        # If current question was answered correctly, remove it from rotation
        if self.current_idx in self.session.correct:
            # Remove from question order if present
            if self.current_idx in self.question_order:
                self.question_order.remove(self.current_idx)
                # Adjust position if we removed an element before current position
                if self.current_position > 0:
                    self.current_position -= 1

        # Move to next question
        self.current_idx = self._get_next_question_idx()

    def get_current_correct_answer(self) -> str:
        """Get the correct answer for current question"""
        if self.current_idx is None:
            return ""
        return self.session.questions[self.current_idx].answer

    def update_statistics(self) -> dict:
        """Get current session statistics"""
        return self.session.get_stats()

    def _get_next_question_idx(self) -> Optional[int]:
        """Get the next question index in rotation"""
        # Filter out correctly answered questions from rotation
        remaining_questions = [idx for idx in self.question_order if idx not in self.session.correct]

        if not remaining_questions:
            return None  # All questions answered correctly

        # Update question order if it has changed
        if len(remaining_questions) != len(self.question_order):
            self.question_order = remaining_questions
            self.current_position = 0

        # Get next question in sequence
        if self.current_position >= len(self.question_order):
            # Reached end, reshuffle and restart for incorrect questions
            random.shuffle(self.question_order)
            self.current_position = 0

        if self.question_order:
            next_idx = self.question_order[self.current_position]
            self.current_position += 1
            return next_idx

        return None
