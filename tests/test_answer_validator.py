"""
Unit tests for AnswerValidator
"""
import pytest
from pyteacher.utils.answer_validator import AnswerValidator


class TestAnswerValidator:

    def test_normalize_input_basic(self):
        """Test basic input normalization"""
        assert AnswerValidator.normalize_input("  Hello World  ") == "hello world"
        assert AnswerValidator.normalize_input("UPPERCASE") == "uppercase"
        assert AnswerValidator.normalize_input("") == ""

    def test_normalize_input_punctuation(self):
        """Test punctuation removal"""
        assert AnswerValidator.normalize_input("hello, world!") == "hello world"
        assert AnswerValidator.normalize_input("it's") == "its"
        assert AnswerValidator.normalize_input("yes-no") == "yesno"

    def test_normalize_input_whitespace(self):
        """Test whitespace normalization"""
        assert AnswerValidator.normalize_input("multiple   spaces") == "multiple spaces"
        assert AnswerValidator.normalize_input("tab\tspace") == "tab space"

    def test_compare_answers_exact(self):
        """Test exact answer comparison"""
        assert AnswerValidator.compare_answers("hello", "hello") is True
        assert AnswerValidator.compare_answers("world", "earth") is False

    def test_compare_answers_case_insensitive(self):
        """Test case insensitive comparison"""
        assert AnswerValidator.compare_answers("Hello", "hello") is True
        assert AnswerValidator.compare_answers("WORLD", "world") is True

    def test_compare_answers_whitespace(self):
        """Test whitespace handling"""
        assert AnswerValidator.compare_answers("  hello  ", "hello") is True
        assert AnswerValidator.compare_answers("hello world", "hello  world") is True

    def test_compare_answers_punctuation(self):
        """Test punctuation handling"""
        assert AnswerValidator.compare_answers("hello, world!", "hello world") is True
        assert AnswerValidator.compare_answers("it's", "its") is True

    def test_handle_special_cases_articles(self):
        """Test article handling"""
        assert AnswerValidator.handle_special_cases("the cat") == "cat"
        assert AnswerValidator.handle_special_cases("a dog") == "dog"
        assert AnswerValidator.handle_special_cases("an apple") == "apple"

    def test_validate_input_valid(self):
        """Test valid input validation"""
        is_valid, msg = AnswerValidator.validate_input("hello")
        assert is_valid is True
        assert msg == ""

    def test_validate_input_empty(self):
        """Test empty input validation"""
        is_valid, msg = AnswerValidator.validate_input("")
        assert is_valid is False
        assert "Please enter an answer" in msg

        is_valid, msg = AnswerValidator.validate_input("   ")
        assert is_valid is False
        assert "Please enter an answer" in msg

    def test_validate_input_too_long(self):
        """Test overly long input validation"""
        long_input = "a" * 201
        is_valid, msg = AnswerValidator.validate_input(long_input)
        assert is_valid is False
        assert "too long" in msg
