#!/usr/bin/python3
"""Definition of Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Create an instance of Review"""
    place_id = ""
    user_id = ""
    text = ""
