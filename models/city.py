#!/usr/bin/python3
"""class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City - inherits from BaseModel - Public class attr - state_id,
         name"""
    state_id = ""
    name = ""
