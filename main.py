from square_generator.cubic_generator import CubicGenerator

cubic_gen = CubicGenerator()

try:
    cubes = cubic_gen.generate_squares(1, 5)
    print("Cubes:", cubes)
except Exception as e:
    print(f"Error: {e}")
