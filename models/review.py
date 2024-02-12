#!/usr/bin/python3
"""import"""
from models.base_model import BaseModel
"""class define"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""
