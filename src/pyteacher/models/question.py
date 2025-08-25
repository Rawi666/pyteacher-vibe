"""
QuestionAnswer dataclass for language learning app
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class QuestionAnswer:
    question: str
    answer: str
    hint: Optional[str] = None
