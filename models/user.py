#!/usr/bin/python3
"""Definition of User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create an instance of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
