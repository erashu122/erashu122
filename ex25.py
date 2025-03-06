#return = statement used to end a function and send a value back to its caller
first = input("Enter your first name: ")
last = input("Enter your last name: ")

def create_name(first ,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+ " " +last

full_name = create_name(first,last) 
print (full_name)

