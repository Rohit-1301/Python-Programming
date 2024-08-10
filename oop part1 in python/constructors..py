class Employee:
    name=""
    age=23
    salary=50000

    def __init__(self,name,age,salary):
        print("")
        print("This is a class to store the information of the employee:- ",name)
        self.name=name
        self.age=age
        self.salary=salary
    
    def getinfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The age of the employee is {self.age}")
        print(f"The salary of the employee is {self.salary}")

name=input("Enter the name of the employee: ")
age=int(input("Enter the age of the employee: "))
salary=float(input("Enter the salary of the employee: "))

Rohit=Employee(name,age,salary)
Rohit.getinfo()
