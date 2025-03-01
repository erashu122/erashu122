tem = float(input("enter the temperature: "))   
is_raining= input("is it raining? (yes/no): ")
is_raining = is_raining.lower() == "yes"

if tem>35 or tem<0 or is_raining:
    print("the outdore activity is not allowed")
    
elif tem>=0 and tem<=35 and not is_raining:
    print("the outdore activity is allowed")
else:
    print("the outdore activity is allowed")