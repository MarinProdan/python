import math
class Kruznice:
    def __init__(self,r=()):
        self.r=r
    
    def ma_obvod(self):
        return 2*3.14*self.r
    def ma_obsah(self):
        return 3.14*(self.r**2)

    def __str__(self):
        return f"Kruznice o polomeru {self.r} má obvod O: {self.ma_obvod()}, a obsah S: {self.ma_obsah()}"
    
k=Kruznice(6)
print(k)