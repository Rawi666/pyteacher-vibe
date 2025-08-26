"""
AnswerValidator for normalizing and comparing user answers
"""
import re
import unicodedata


class AnswerValidator:
    """Handles answer validation and normalization"""

    @staticmethod
    def normalize_input(user_input: str) -> str:
        """Normalize user input for comparison"""
        if not user_input:
            return ""

        # Remove leading/trailing whitespace
        normalized = user_input.strip()

        # Convert to lowercase
        normalized = normalized.lower()

        # Normalize unicode characters (decompose accents)
        normalized = unicodedata.normalize('NFD', normalized)

        # Remove diacritical marks
        normalized = ''.join(
            char for char in normalized
            if unicodedata.category(char) != 'Mn'
        )

        # Normalize whitespace (replace multiple spaces with single space)
        normalized = re.sub(r'\s+', ' ', normalized)

        # Remove common punctuation
        normalized = re.sub(r'[.,!?;:\'"\-_]', '', normalized)

        return normalized.strip()

    @staticmethod
    def compare_answers(user_answer: str, correct_answer: str) -> bool:
        """Compare user answer with correct answer after normalization"""
        normalized_user = AnswerValidator.normalize_input(user_answer)
        normalized_correct = AnswerValidator.normalize_input(correct_answer)

        if not normalized_user or not normalized_correct:
            return False

        return normalized_user == normalized_correct

    @staticmethod
    def handle_special_cases(answer: str) -> str:
        """Handle special cases in answers"""
        # Handle articles in different languages
        articles = ['the', 'a', 'an', 'der', 'die', 'das', 'le', 'la', 'les', 'el', 'la', 'los', 'las']

        normalized = AnswerValidator.normalize_input(answer)
        words = normalized.split()

        # Remove leading articles
        if words and words[0] in articles:
            words = words[1:]

        return ' '.join(words)

    @staticmethod
    def validate_input(user_input: str) -> tuple[bool, str]:
        """Validate user input and return (is_valid, error_message)"""
        if not user_input or not user_input.strip():
            return False, "Please enter an answer"

        if len(user_input.strip()) > 200:
            return False, "Answer is too long"

        return True, ""
