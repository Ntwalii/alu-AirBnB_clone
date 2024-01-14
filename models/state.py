#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

# State inherits from BaseModel
class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
