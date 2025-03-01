def print_normal_pyramid(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

# Test the function
print_normal_pyramid(5)