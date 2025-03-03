#dictionary= a collaction of{key:value} pairs
#ordered, changeable and does not allow duplicates
import random

capital = {
    "India": "Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Russia": "Moscow",
    "Brazil": "Brasilia",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "South Africa": "Pretoria",
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "Mexico": "Mexico City",
    "Argentina": "Buenos Aires",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka",
    "Indonesia": "Jakarta",
    "Philippines": "Manila",
    "Vietnam": "Hanoi",
    "Thailand": "Bangkok",
    "Malaysia": "Kuala Lumpur",
    "Singapore": "Singapore",
    "Saudi Arabia": "Riyadh",
    "Turkey": "Ankara",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Syria": "Damascus",
}

# print(capital.get("India"))
# if capital.get("India"):
#     print("India is present in the dictionary")
# else:
#     print("India is not present in the dictionary")

capital.update({"Afghanistan": "Kabul"})
print(capital.get("Afghanistan"))
    
