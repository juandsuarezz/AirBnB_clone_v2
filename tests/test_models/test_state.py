#!/usr/bin/python3
""" """
import os
import unittest
from models.base_model import BaseModel, Base
from models.state import State


class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_State_inheritence(self):
        """Test that State class inherits from BaseModel"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)
