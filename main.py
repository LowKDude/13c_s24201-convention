def generate_squares(start, end):
    squares = [x ** 2 for x in range(start, end)]
    return squares

start = 1
end = 11
squares_list = generate_squares(start, end)

print("List of squares of numbers from {} to {}:".format(start, end - 1))
print(squares_list)
