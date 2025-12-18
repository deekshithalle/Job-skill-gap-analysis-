from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    name: str
    target_role: str
    current_skills: List[str]
