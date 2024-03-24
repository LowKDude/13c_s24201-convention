from .square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if not start < end:
            raise Exception("The start of the range must be less than the end.")
        return [x**3 for x in range(start, end + 1)]
