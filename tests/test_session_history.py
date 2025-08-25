"""
Unit tests for SessionHistory
"""
from pyteacher.utils.session_history import SessionHistory
import tempfile
import os

def test_add_and_get_history():
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.close()
    history = SessionHistory(tmp_file.name)
    session_data = {"total": 10, "learned": 5}
    history.add_session(session_data)
    assert history.get_history()[-1] == session_data
    os.remove(tmp_file.name)
