#sopping cart program


foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)
        
print("-----------YOUR CART-----------")
for food in foods:
    print(food,end=" ")
    
for price in prices:
    total += price
    
print(f"\nyour total is: ${total:.2f}")

# # Calculate the total price
# total = sum(prices)

# # Print the shopping list and total price
# print("\nShopping List:")
# for i in range(len(foods)):
#     print(f"{foods[i]}: ${prices[i]:.2f}")

# print(f"\nTotal: ${total:.2f}")