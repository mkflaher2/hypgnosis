from enum import Enum
from pydantic import BaseModel

from datetime import datetime
import time

class Color(BaseModel):
    r: float = 1
    g: float = 1
    b: float = 1
    a: float = 1

class ControlModel(BaseModel):
    user_id: str = None
    speed: float = 1
    color:Color = Color()
    last_updated: float = time.mktime(datetime.now().timetuple())

    def set_user_id(self, user_id: str):
        self.user_id = user_id
