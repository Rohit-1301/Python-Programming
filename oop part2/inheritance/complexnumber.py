# it is a problem to print the sum of two complex number
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, c1):
        print("The addition of the two complex numbers is:")
        return Complex(self.real + c1.real, self.img + c1.img)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
