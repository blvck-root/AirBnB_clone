#!/usr/bin/python3
"""import module"""

from models.base_model import BaseModel
"""defines class"""


class City(BaseModel):
    state_id: str = ""
    name: str = ""
