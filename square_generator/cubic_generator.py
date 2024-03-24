from .square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if end < start:
            start, end = end, start
        return [x**3 for x in range(start, end + 1)]
