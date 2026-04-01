from pydantic import BaseModel
from typing import List, Dict

class Observation(BaseModel):
    disaster_type: str
    areas: List[Dict]
    resources: Dict

class Action(BaseModel):
    allocations: List[Dict]
    reasoning: str

class Reward(BaseModel):
    score: float