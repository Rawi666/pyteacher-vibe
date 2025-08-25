"""
Unit tests for DataLoader
"""
import pytest
from pyteacher.utils.data_loader import DataLoader

class TestDataLoader:
    def test_validate_json_structure_valid(self):
        data = [{"question": "Q1", "answer": "A1"}, {"question": "Q2", "answer": "A2"}]
        assert DataLoader.validate_json_structure(data) is True

    def test_validate_json_structure_invalid(self):
        data = [{"question": "Q1"}, {"answer": "A2"}]
        assert DataLoader.validate_json_structure(data) is False
