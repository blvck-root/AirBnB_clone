#!/usr/bin/python3
"""class define"""


class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""
