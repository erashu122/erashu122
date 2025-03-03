#python compound interest calculator
#compound interest formula: A=P(1+r/n)^nt

principal=0
rate=0
time=0
while principal<=0:
    principal = float(input("enter the principal amount: "))   
    if principal< 0:
        print("the principal amount should be greater than 0")
        
while rate<=0:
    rate = float(input("enter the rate of interest: "))
    if rate< 0:
        print("the rate of interest should be greater than 0")
        
while time<=0:
    time = float(input("enter the time in years: "))
    if time< 0:
        print("the time should be greater than 0")

total =principal* pow((1+rate/100),time)
print (f"Balance after {time} years is ${total:.2f}")           