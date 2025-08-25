"""
Unit tests for FileManager
"""
from pyteacher.utils.file_manager import FileManager
import tempfile
import os

class DummyParent:
    pass

def test_validate_file_valid():
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as tmp:
        tmp.write(b'{}')
        tmp.flush()
        assert FileManager.validate_file(tmp.name)
    os.remove(tmp.name)

def test_validate_file_invalid():
    assert not FileManager.validate_file('nonexistent.json')
    assert not FileManager.validate_file('invalid.txt')
