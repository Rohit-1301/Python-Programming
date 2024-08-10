class Employee:
    company="Microsoft"
    def _init_(self):
        print("The name of the employee is ",self.company);

class Programmer(Employee):
    company="Youtube"
        
    def show(self):
        print("The name of the employee is ",self.company)
    
n=Employee();
s=Programmer();

print(s.company)

print(n.company)