# question to convet celcius to farheneit
# def farheneit(celcius):
#     return celcius * 9/5 + 32;

# celcius = float(input("enter the celcius value: "))
# print(f"the farheneit value is: {farheneit(celcius)} ")

# sum of first n natural number
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)
# n=int(input("enter the number whose sum u want: "))
# print(f"the sum of the number is: {sum(n)}")

# recursive function to print star
def star(n):
    if n == 0:
        return
    print("*"*n)
    star(n-1)

n=int(input("enter the number of star u want: "))
star(n)