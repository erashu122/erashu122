unit = input("is this temperature in celsius or fahrenheit? (c/f): ")
temp = float(input("enter the temperature: "))
is_sunny = input("is it sunny? (yes/no): ")
if unit == "c":
    result = (temp * 9/5) + 32
    print(f"{temp} celsius is {result} fahrenheit 🌡️")
elif unit == "f":
    result = (temp - 32) * 5/9
    print(f"{temp} fahrenheit is {result} celsius 🌡️")
else:
    print(f"you are giving the wrong {unit} unit ❌")
    
if result >= 28 and is_sunny == "yes":
    print("it is HOT outside ☀️")
    print("it is sunny 🌞")
elif result >= 28 and is_sunny == "no":
    print("it is WARM outside 🌤️")
    print("it is not sunny 🌥️")
elif result < 28 and is_sunny == "yes":
    print("it is COLD outside ❄️")
    print("it is sunny 🌞")
elif result < 28 and is_sunny == "no":
    print("it is CHILLY outside 🥶")
    print("it is not sunny 🌥️")
else:
    print("the outdoor activity is allowed ✅")