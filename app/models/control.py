from enum import Enum
from pydantic import BaseModel

class Color(BaseModel):
    r: float = 1
    g: float = 1
    b: float = 1
    a: float = 1


class ControlModel(BaseModel):
    direction: int = 1
    speed: float = 1
    color:Color = Color()

