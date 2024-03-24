class SquareGenerator:
    def generate_squares(self, start, end):

        return [x**2 for x in range(start, end + 1)]

# Example usage
square_gen = SquareGenerator()
squares = square_gen.generate_squares(1, 10)
print(squares)
