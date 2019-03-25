#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review - inherits from BaseModel - Public class attr - email,
    text, user_id, place_id"""
    place_id = ""
    user_id = ""
    text = ""
