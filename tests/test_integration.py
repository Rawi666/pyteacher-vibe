"""
Integration tests for complete drill workflow
"""
import pytest
import tempfile
import json
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from pyteacher.ui.drill_window import DrillWindow
from pyteacher.controllers.drill_controller import DrillController
from pyteacher.models.question import QuestionAnswer
import sys


class TestDrillWorkflow:

    @pytest.fixture(autouse=True)
    def setup_app(self):
        """Setup QApplication for GUI tests"""
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
        yield

    @pytest.fixture
    def sample_json_file(self):
        """Create a temporary JSON file with sample questions"""
        questions = [
            {"question": "What is 2+2?", "answer": "4"},
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What color is the sky?", "answer": "blue"}
        ]

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(questions, f)
            temp_file = f.name

        yield temp_file

        # Cleanup
        if os.path.exists(temp_file):
            os.unlink(temp_file)

    def test_drill_controller_complete_flow(self):
        """Test complete drill controller workflow"""
        questions = [
            QuestionAnswer("What is 2+2?", "4"),
            QuestionAnswer("What is the capital of France?", "Paris")
        ]

        controller = DrillController(questions)
        controller.start_drill()

        # Initial state
        assert controller.current_idx is not None
        stats = controller.update_statistics()
        assert stats['total'] == 2
        assert stats['learned'] == 0
        assert stats['left'] == 2

        # Answer first question correctly
        current_q = controller.session.questions[controller.current_idx]
        correct = controller.check_answer(current_q.answer)
        assert correct is True

        # Move to next question
        controller.next_question()
        stats = controller.update_statistics()
        assert stats['learned'] == 1
        assert stats['left'] == 1

        # Answer second question correctly
        if controller.current_idx is not None:
            current_q = controller.session.questions[controller.current_idx]
            correct = controller.check_answer(current_q.answer)
            assert correct is True

            controller.next_question()
            stats = controller.update_statistics()
            assert stats['learned'] == 2
            assert stats['left'] == 0
            assert controller.current_idx is None  # All questions completed

    def test_drill_controller_incorrect_answers(self):
        """Test drill controller with incorrect answers"""
        questions = [
            QuestionAnswer("What is 2+2?", "4"),
        ]

        controller = DrillController(questions)
        controller.start_drill()

        # Give wrong answer
        correct = controller.check_answer("wrong")
        assert correct is False

        # Question should remain in rotation
        controller.next_question()
        stats = controller.update_statistics()
        assert stats['learned'] == 0
        assert stats['left'] == 1
        assert controller.current_idx is not None

    def test_drill_window_esc_key(self):
        """Test ESC key functionality in drill window"""
        window = DrillWindow()
        window.show()

        # Simulate ESC key press
        QTest.keyPress(window, Qt.Key.Key_Escape)

        # Window should be closed (we can't easily test window manager integration here)
        # Just verify that the key event is handled without errors

    def test_answer_normalization_in_controller(self):
        """Test answer normalization in controller"""
        questions = [
            QuestionAnswer("What is the capital?", "Paris"),
            QuestionAnswer("What is 2+2?", "4"),  # Add second question to avoid completion
        ]

        controller = DrillController(questions)
        controller.start_drill()

        # Find the Paris question
        paris_question_idx = None
        for i, q in enumerate(questions):
            if "capital" in q.question:
                paris_question_idx = i
                break

        # Set current question to the Paris question for testing
        controller.current_idx = paris_question_idx

        # Test various input formats
        assert controller.check_answer("paris") is True

        # Reset and test again
        controller.session.correct.clear()  # Clear correct answers
        controller.current_idx = paris_question_idx
        assert controller.check_answer("  PARIS  ") is True

        # Reset and test again
        controller.session.correct.clear()  # Clear correct answers
        controller.current_idx = paris_question_idx
        assert controller.check_answer("Paris!") is True

    def test_drill_window_feedback_flow(self):
        """Test feedback flow requiring ENTER key press to proceed"""
        window = DrillWindow()
        window.show()

        # Create sample questions for testing
        questions = [
            QuestionAnswer("Test question 1", "answer1"),
            QuestionAnswer("Test question 2", "answer2")
        ]

        # Set up controller directly for testing
        from pyteacher.controllers.drill_controller import DrillController
        window.controller = DrillController(questions)
        window.controller.start_drill()
        window.questions = questions
        window._update_ui()

        # Initially should not be in feedback mode
        assert window.waiting_for_feedback_enter is False
        assert window.answer_edit.isReadOnly() is False

        # Type an answer
        window.answer_edit.setText("wrong answer")

        # Simulate ENTER key press to submit answer
        QTest.keyPress(window.answer_edit, Qt.Key.Key_Return)

        # Should now be in feedback mode
        assert window.waiting_for_feedback_enter is True
        assert window.answer_edit.isReadOnly() is True

        # Simulate ENTER key press to proceed (should advance to next question)
        QTest.keyPress(window.answer_edit, Qt.Key.Key_Return)

        # Should no longer be in feedback mode
        assert window.waiting_for_feedback_enter is False
        assert window.answer_edit.isReadOnly() is False

        window.close()

    def test_test_window_feedback_flow(self):
        """Test feedback flow in test window requiring ENTER key press to proceed"""
        from pyteacher.ui.test_window import TestWindow

        window = TestWindow()
        window.show()

        # Create sample questions for testing
        questions = [
            QuestionAnswer("Test question 1", "answer1"),
            QuestionAnswer("Test question 2", "answer2")
        ]

        # Set up controller directly for testing
        from pyteacher.controllers.test_controller import QuizTestController
        window.controller = QuizTestController(questions)
        window.controller.start_test()
        window.questions = questions
        window._update_ui()

        # Initially should not be in feedback mode
        assert window.waiting_for_feedback_enter is False
        assert window.answer_edit.isReadOnly() is False

        # Type an answer
        window.answer_edit.setText("wrong answer")

        # Simulate ENTER key press to submit answer
        QTest.keyPress(window.answer_edit, Qt.Key.Key_Return)

        # Should now be in feedback mode
        assert window.waiting_for_feedback_enter is True
        assert window.answer_edit.isReadOnly() is True

        # Simulate ENTER key press to proceed (should advance to next question)
        QTest.keyPress(window.answer_edit, Qt.Key.Key_Return)

        # Should no longer be in feedback mode
        assert window.waiting_for_feedback_enter is False
        assert window.answer_edit.isReadOnly() is False

        window.close()
