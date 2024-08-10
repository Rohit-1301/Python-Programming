class Number:
    def __init__(self,num) :
        self.num=num

    def __add__(self,num2):
            print("Lets add")
            return self.num+num2.num
    
    def __sub__(self,num2):
            print("Lets sub")
            return self.num-num2.num
    
    def __mul__(self,num2):
            print("Lets multiply")
            return self.num*num2.num
    
    def __truediv__(self,num2):
            print("Lets divide")
            return self.num/num2.num
    
    def __floordiv__(self,num2):
            print("Lets floor divide")
            return self.num//num2.num
    
    # def __str__(self) -> str:
    #     return f"Decimal Number : {self.num}"
    
    # def __init__(self, your_string):
    #     self.your_string = your_string

    # def __len__(self) -> int:
    #     return len(self.your_string)
    

n=Number(5)
m=Number(6)
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)

# s="Rohit Gupta"
# m="Aditya Singh"



