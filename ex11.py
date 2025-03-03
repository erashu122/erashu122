row = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to use: ")

for i in range(row):
    # Print leading spaces
    for j in range(row - i - 1):
        print(" ", end="")
    # Print symbols
    for k in range(2 * i + 1):
        print(symbol, end="")
    # Move to the next line
    print()