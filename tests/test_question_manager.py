"""
Unit tests for QuestionManager
"""
from pyteacher.models.question import QuestionAnswer
from pyteacher.models.question_manager import QuestionManager

class TestQuestionManager:
    def test_session_statistics(self):
        questions = [QuestionAnswer("Q1", "A1"), QuestionAnswer("Q2", "A2")]
        manager = QuestionManager(questions)
        assert manager.get_session_statistics()["total"] == 2
        manager.mark_question_correct(0)
        assert manager.get_session_statistics()["learned"] == 1
        assert manager.get_session_statistics()["left"] == 1
