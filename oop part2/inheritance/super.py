class Employee:
    Company="Microsoft"
    def __init__(self) -> None:
        print("It is a constructor of class Employee")
    def company(self):
        print("The name of the company is ",self.Company);

class Programmer(Employee):
    Role="Full Stack Development"
    def __init__(self) -> None:
        super().__init__()
        print("It is a constructor of class Programmer")
    def role(self):
        print("The role of the employee is ",self.Role)

class Coder(Programmer):
    Technology="React"
    def __init__(self) -> None:
        super().__init__()
        print("It is a constructor of class Coder")
    def technology(self):
        print("Technology on which the employee work is ",self.Technology)

s=Employee();
s.company();
print("")

t=Programmer();
t.company();
t.role();
print("")

u=Coder();
u.company();
u.role();
u.technology();