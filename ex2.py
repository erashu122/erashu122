# simple calculater

operator = input("enter the operator (- + * /) :")
num1 = float(input("enter the first number:"))
num2 = float(input("enter second number:"))

if operator == "+":
    result = num1+num2
    print(round(result, 3))
elif operator == "-":
    result = num1-num2
    print(round(result, 3))
elif operator == "*":
    result = num1*num2
    print(round(result, 3))
elif operator == "/":
    result = num1/num2
    print(round(result, 3))
else :
    print(f"you are giving the worng {operator} operator")
