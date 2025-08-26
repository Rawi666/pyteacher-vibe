"""
Unit tests for DataLoader
"""
import pytest
from pyteacher.utils.data_loader import DataLoader

class TestDataLoader:
    def test_validate_json_structure_valid(self):
        data = [{"question": "Q1", "answer": "A1"}, {"question": "Q2", "answer": "A2"}]
        is_valid, error_msg = DataLoader.validate_json_structure(data)
        assert is_valid is True
        assert error_msg == ""

    def test_validate_json_structure_invalid(self):
        data = [{"question": "Q1"}, {"answer": "A2"}]
        is_valid, error_msg = DataLoader.validate_json_structure(data)
        assert is_valid is False
        assert "missing fields" in error_msg
