
from dataclasses import dataclass, field

@dataclass
class Point:
    z: list =[]
    
    x:float
    
    def __post_init__(self):
