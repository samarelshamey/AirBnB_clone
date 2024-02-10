#!/usr/bin/python3
"""the User class module"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class

    Attributes:
        email: user email
        password: password
        firs_name: user first name
        last_name: user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
