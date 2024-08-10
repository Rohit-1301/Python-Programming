# list = [1,2,3,4,5]

# squareslist=[]
# for i in list:
#     squareslist.append(i*i)

# print(squareslist)

# squaredlist=[i*i for i in list]
# print(squaredlist)

n=int(input("Enter the number whose table you want to print: "))
table=[i*n for i in range(1,11)]
print(table)