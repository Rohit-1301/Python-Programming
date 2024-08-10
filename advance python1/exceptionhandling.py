
try:
    a=int(input("enter the value of a: "))
    print(a)
except Exception as e:
    print(e)
finally:
    print("i am always executed")

# if we use try else syntax the else block will run if it is error doesn't catch else it not
# while finally block will run even exception cattch or not
# we use finally keyword because if we put any try catch in a function and it return any parameter then also it will work
