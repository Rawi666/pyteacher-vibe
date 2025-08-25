"""
SessionHistory for storing and retrieving session data
"""
import json
from typing import List, Dict

class SessionHistory:
    def __init__(self, file_path: str = "session_history.json"):
        self.file_path = file_path
        self.history: List[Dict] = []
        self._load()

    def _load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.history = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.history = []

    def add_session(self, session_data: Dict):
        self.history.append(session_data)
        self._save()

    def _save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def get_history(self) -> List[Dict]:
        return self.history
