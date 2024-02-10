#!/usr/bin/python3
"""the City class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class

    Attributes:
        state_id: state id
        name: name of city
    """

    state_id = ""
    name = ""
