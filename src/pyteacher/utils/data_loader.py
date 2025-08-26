"""
DataLoader for loading and validating JSON question files
"""
import json
from typing import List, Tuple
from ..models.question import QuestionAnswer


class DataLoader:
    @staticmethod
    def load_json_file(file_path: str) -> List[QuestionAnswer]:
        """Load questions from JSON file with comprehensive error handling"""
        data = DataLoader._read_json_file(file_path)
        DataLoader._validate_data_structure(data)
        return DataLoader._convert_to_questions(data)

    @staticmethod
    def _read_json_file(file_path: str) -> list:
        """Read and parse JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
        except UnicodeDecodeError:
            raise ValueError("File encoding not supported. Please use UTF-8.")
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")
        return data

    @staticmethod
    def _validate_data_structure(data) -> None:
        """Validate the basic structure of loaded data"""
        if not isinstance(data, list):
            raise ValueError("JSON file must contain a list of questions")
        if not data:
            raise ValueError("JSON file is empty")

    @staticmethod
    def _convert_to_questions(data: list) -> List[QuestionAnswer]:
        """Convert data items to QuestionAnswer objects"""
        questions = []
        for i, item in enumerate(data):
            DataLoader._validate_question_item(item, i + 1)
            try:
                question = QuestionAnswer(**item)
                questions.append(question)
            except Exception as e:
                raise ValueError(f"Error creating question {i+1}: {e}")
        return questions

    @staticmethod
    def _validate_question_item(item, item_number: int) -> None:
        """Validate a single question item"""
        if not isinstance(item, dict):
            raise ValueError(f"Item {item_number} must be an object")

        if 'question' not in item:
            raise ValueError(f"Item {item_number} missing 'question' field")

        if 'answer' not in item:
            raise ValueError(f"Item {item_number} missing 'answer' field")

        if not isinstance(item['question'], str) or not item['question'].strip():
            raise ValueError(f"Item {item_number} 'question' must be a non-empty string")

        if not isinstance(item['answer'], str) or not item['answer'].strip():
            raise ValueError(f"Item {item_number} 'answer' must be a non-empty string")

    @staticmethod
    def validate_json_structure(data: list) -> Tuple[bool, str]:
        """Validate JSON structure and return (is_valid, error_message)"""
        if not isinstance(data, list):
            return False, "Data must be a list"

        if not data:
            return False, "List cannot be empty"

        required_keys = {"question", "answer"}
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                return False, f"Item {i+1} must be an object"

            if not required_keys.issubset(item.keys()):
                missing = required_keys - item.keys()
                return False, f"Item {i+1} missing fields: {', '.join(missing)}"

            if not isinstance(item['question'], str) or not item['question'].strip():
                return False, f"Item {i+1} 'question' must be a non-empty string"

            if not isinstance(item['answer'], str) or not item['answer'].strip():
                return False, f"Item {i+1} 'answer' must be a non-empty string"

        return True, ""

    @staticmethod
    def get_file_info(file_path: str) -> dict:
        """Get basic information about the JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            is_valid, error = DataLoader.validate_json_structure(data)

            return {
                'valid': is_valid,
                'error': error,
                'question_count': len(data) if isinstance(data, list) else 0,
                'file_size': len(str(data)),
            }
        except Exception as e:
            return {
                'valid': False,
                'error': str(e),
                'question_count': 0,
                'file_size': 0,
            }
