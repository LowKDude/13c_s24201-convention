# square_generator.py
import math


class SquareGenerator:
    def generate_squares(self, start, end):

        if end < start:
            start, end = end, start  # Swap values to ensure a valid range
        return [x ** 2 for x in range(start, end + 1)]

    def square_roots(self, numbers):

        return [math.sqrt(number) for number in numbers]
