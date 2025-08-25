"""
Unit tests for StatisticsCalculator
"""
from pyteacher.utils.statistics import StatisticsCalculator

class TestStatisticsCalculator:
    def test_calculate_accuracy(self):
        assert StatisticsCalculator.calculate_accuracy(5, 10) == 50.0
        assert StatisticsCalculator.calculate_accuracy(0, 0) == 0.0

    def test_format_session_time(self):
        assert StatisticsCalculator.format_session_time(125) == "2m 5s"

    def test_generate_performance_report(self):
        stats = {"total": 10, "learned": 5}
        report = StatisticsCalculator.generate_performance_report(stats)
        assert report["accuracy"] == "50.00%"
