from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
squares = square_gen.generate_squares(1, 10)
print("Squares:", squares)

square_roots = square_gen.square_roots(squares)
print("Square Roots:", square_roots)
