import math


class SquareGenerator:
    def generate_squares(self, start, end):

        return [x ** 2 for x in range(start, end + 1)]

    def square_roots(self, numbers):

        return [math.sqrt(number) for number in numbers]


# Example usage
square_gen = SquareGenerator()
squares = square_gen.generate_squares(1, 10)
print("Squares:", squares)

square_roots = square_gen.square_roots(squares)
print("Square Roots:", square_roots)
