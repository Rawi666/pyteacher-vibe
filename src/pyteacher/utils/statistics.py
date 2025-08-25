"""
Statistics utility for session performance
"""
from typing import Dict

class StatisticsCalculator:
    @staticmethod
    def calculate_accuracy(correct: int, total: int) -> float:
        if total == 0:
            return 0.0
        return (correct / total) * 100

    @staticmethod
    def format_session_time(seconds: int) -> str:
        mins, secs = divmod(seconds, 60)
        return f"{mins}m {secs}s"

    @staticmethod
    def generate_performance_report(stats: Dict[str, int]) -> Dict[str, str]:
        accuracy = StatisticsCalculator.calculate_accuracy(stats.get("learned", 0), stats.get("total", 0))
        return {
            "total": str(stats.get("total", 0)),
            "correct": str(stats.get("learned", 0)),
            "accuracy": f"{accuracy:.2f}%"
        }
