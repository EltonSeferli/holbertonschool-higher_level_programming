#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
