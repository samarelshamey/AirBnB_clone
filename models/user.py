#!/usr/bin/python3
"""the User class module"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
