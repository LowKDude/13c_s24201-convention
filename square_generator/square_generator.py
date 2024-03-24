# square_generator.py
from abc import ABC, abstractmethod
import math

class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):

        pass
