a=int(input("enter a number a: "))
b=int(input("enter a number b: "))

if b==0:
    raise ZeroDivisionError("you cannot divide a number by 0")
else:
    print(a/b)


    