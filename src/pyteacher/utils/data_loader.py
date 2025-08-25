"""
DataLoader for loading and validating JSON question files
"""
import json
from typing import List
from ..models.question import QuestionAnswer

class DataLoader:
    @staticmethod
    def load_json_file(file_path: str) -> List[QuestionAnswer]:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [QuestionAnswer(**item) for item in data]

    @staticmethod
    def validate_json_structure(data: list) -> bool:
        required_keys = {"question", "answer"}
        for item in data:
            if not required_keys.issubset(item.keys()):
                return False
        return True
