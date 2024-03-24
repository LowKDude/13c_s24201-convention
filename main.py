# Assuming `square_generator.py` is in the same directory as this script
from square_generator import SquareGenerator

# Example usage
square_gen = SquareGenerator()
squares = square_gen.generate_squares(1, 10)
print("Squares:", squares)

square_roots = square_gen.square_roots(squares)
print("Square Roots:", square_roots)
