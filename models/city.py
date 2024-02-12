#!/usr/bin/python3
"""defines class"""

from models.base_model import BaseModel

class City(BaseModel):
    state_id: str = ""
    name: str = ""
