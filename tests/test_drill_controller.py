"""
Unit tests for DrillController
"""
from pyteacher.models.question import QuestionAnswer
from pyteacher.controllers.drill_controller import DrillController

def test_drill_controller_flow():
    questions = [QuestionAnswer("Q1", "A1"), QuestionAnswer("Q2", "A2")]
    controller = DrillController(questions)
    controller.start_drill()
    idx = controller.current_idx
    assert controller.check_answer("A1") is True or controller.check_answer("A2") is True
    controller.next_question()
    assert controller.current_idx in [0, 1]
    stats = controller.update_statistics()
    assert stats["total"] == 2
