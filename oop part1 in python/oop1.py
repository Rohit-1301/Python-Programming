class Employee:
    name="Rohit"
    id="123456"
    salary="5600000"

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    def getinfo(self):
        print(f"The name of the employee is {self.name}")
        print(f"The id of the employee is {self.id}")
        print(f"The salary of the employee is {self.salary}")

Rohit=Employee()
Rohit.greet()
Rohit.getinfo()


# instance attributes take more priority than the class attribute 