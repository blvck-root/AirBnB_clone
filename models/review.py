#!/usr/bin/python3
"""import"""
from models.base_model import BaseModel
"""class define"""


class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""
