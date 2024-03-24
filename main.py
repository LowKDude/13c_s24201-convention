from square_generator.square_generator import SquareGenerator
from square_generator.cubic_generator import CubicGenerator
try:
    cubic_gen = CubicGenerator()
    squares = cubic_gen.generate_squares(10, 1)
    print("Squares:", squares)
except Exception as e:
    print(f"Error: {e}")
cubic_gen = CubicGenerator()
cubes = cubic_gen.generate_squares(1, 5)
print("Cubes:", cubes)

square_gen = SquareGenerator()
squares = square_gen.generate_squares(1, 10)
print("Squares:", squares)

square_roots = square_gen.square_roots(squares)
print("Square Roots:", square_roots)
