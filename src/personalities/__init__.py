from .luna import luna
from .sacha import sacha
from .lucas import qiuxiao # 这是你的新人格

__all__ = [
    "sacha"、
    "luna"、
    "qiuxiao", # 在这里添加你的个性
    "get_personality"
]
from pathlib import Path
from typing import List, Dict, Optional

from pydantic import BaseModel
from urllib3.util import Url

dir_path = Path(__file__).parent

# Get a list of all Python files in the directory
personality_files = dir_path.glob("*.json")


class Personality(BaseModel):
    name: str
    byline: str
    identity: List[str]
    behavior: List[str]
    profile_image: Optional[str]


personalities: Dict[str, Personality] = {}
for personality_file in personality_files:
    personality = Personality.parse_file(personality_file)
    personalities[personality_file.stem] = personality


def get_personality(name: str):
    try:
        return {
            "luna": luna,
            "sacha": sacha,
            "lucas": qiuxiao  # Add your personality here
        }[name]
    except Exception:
        raise Exception("The personality you selected does not exist!")
