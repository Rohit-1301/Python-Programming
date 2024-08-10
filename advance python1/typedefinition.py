# it is used for us to indicate a fellow programmer to understand the type of the variables

def sum(a:int,b:int) ->int:
    return a+b

a:int=int(input("enter the value of a: "))
b:int=int(input("enter the value of b: "))
print(a.bit_length())

print(sum(a,b))