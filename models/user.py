#!/usr/bin/python3
"""class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User - inherits from BaseModel - Public class attr - email,
    password, first_name, last_name"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
