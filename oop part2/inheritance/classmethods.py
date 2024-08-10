class A:
    a=1

    @classmethod
    def classmethod(cls):
        print(cls.a)

    @property
    def name(self):
       return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


s=A();
s.a=5;
# s.classmethod()
s.name="Rohit Gupta"
print(s.fname,s.lname)
print(s.fname)
print(s.lname)








