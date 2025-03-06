#default argument= a default value for ceertain paramiters default is used e=when that argument is omitted make your functions more flexiblew ,redues #of arguments 
#1. position argument= a argument that is passed to a function by its position in the function call
#2. keyword argument= an argument that is passed to a function by its name in the function call 
#3. keyword-only argument= an argument that can only be passed by its name in the function call
#4. arbitrary argument list= a parameter that accepts any number of arguments

def net_price(list_price,discount  ,tax):
    return list_price*(1-discount)*(1+tax)

# print(net_price(500,0,0.05))
# print(net_price(500))
print(net_price(500,0.5,0.06))