row =int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(row):
    for y in range(col):
        print(symbol, end="")
    print()
    