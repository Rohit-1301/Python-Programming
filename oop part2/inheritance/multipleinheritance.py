class Employee:
    Company="Microsoft"
    def company(self):
        print("The name of the company is ",self.Company);

class Programmer:
    Role="Full Stack Development"
        
    def role(self):
        print("The role of the employee is ",self.Role)

class Coder(Employee,Programmer):
    Technology="React"

    def technology(self):
        print("Technology on which the employee work is is ",self.Technology)


s=Coder()
s.company()
s.role()
s.technology()


