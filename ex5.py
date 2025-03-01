#conditional expressions = a one line shortcurt for the if else statement(ternary operator)print or assign value based on a condition x if condition else y
# if else elif

num1 = int(input("enter the first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
age=int(input("enter your age:"))
print (" your number is positive" if num1>0 else "your number is negative")
result ="even" if num1%2==0 else "odd"
print(result)
max = num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
print("the maximum number is",max)
print("you are a minor" if age<18 else "you are an adult")
print("you are a minor" if age<18 else "you are an adult" if age>=18 else "you are a senior")   
min = num1 if num1<num2 and num1<num3 else num2 if num2<num3 else num3
print("the minimum number is",min)
print("the numbers are equal" if num1==num2==num3 else "the numbers are not equal") 
