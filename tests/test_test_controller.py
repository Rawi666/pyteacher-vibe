"""
Unit tests for TestController
"""
from pyteacher.models.question import QuestionAnswer
from pyteacher.controllers.test_controller import TestController

def test_test_controller_flow():
    questions = [QuestionAnswer("Q1", "A1"), QuestionAnswer("Q2", "A2")]
    controller = TestController(questions)
    controller.start_test()
    idx = controller.current_idx
    assert controller.check_answer("A1") is True or controller.check_answer("A2") is True
    controller.next_question()
    assert controller.current_idx in [0, 1]
    stats = controller.update_statistics()
    assert stats["total"] == 2
