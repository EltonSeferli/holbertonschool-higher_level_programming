#!/usr/bin/env python3
"""Pickling Custom Classes"""

import pickle


class CustomObject:
    """Custom object with serialization support"""

    def __init__(self, name, age, is_student):
        """Initialize object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to file using pickle"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file using pickle"""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None
