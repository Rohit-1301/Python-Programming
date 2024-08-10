# def average(a,b,c):
#     print("the average of the three numbers is",(a+b+c)/3);

# a=int(input("enter the first number: "));
# b=int(input("enter the second number: "));
# c=int(input("enter the third number: "));
# average(a,b,c);

def fact(n):
    if(n==1):
        return 1;
    else:
        return n*fact(n-1);

n=int(input("enter the number whose factorial u want: "))
print(f"the factorial of the number is: {fact(n)}");

def fibo(k):
    if(k<=1):
        return k;
    else:
        return fibo(k-1)+fibo(k-2);

k=int(input("enter the number whose fibonacci term you want: "))
print(f"the fibonacci term of the number is: {fibo(k)}");
sum=0;
for i in range(0,k+1):
    sum=sum+fibo(i);

print(f"the sum of the fibonacci term is: {sum}");