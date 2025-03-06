
menu = {
    "hotdog": 2.00,
    "popcorn": 1.50,
    "soda": 1.00,
    "candy": 1.25,
    "water": 1.00,
    "chips": 1.00,
    "cookie": 1.50,
    "fruit": 1.50,
    "nachos": 2.00,
    "pretzel": 1.50,
    "ice cream": 2.00,
    "pickle": 1.00,
    "cotton candy": 1.50,}

cart = []
total = 0
print("--------MENU--------")

for key ,valu  in menu.items():
    print(f"{key} : ${valu:2f}")
    
print("--------------------------")

while True:
    food = input("Enter your item then (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----Your Order-----")
for item in cart:
    total += menu[item]
    print(food,end=" ")
    
print()
print(f"Total: ${total:.2f}")
     
 
        

    

