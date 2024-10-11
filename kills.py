class fighter:
    def __init__(self,name,xp=0):
        self.name = name
        self.xp = int(xp)
    def get_xp(self):
        return self.xp
class fight:
     def __init__(self,f1,f2):
        self.f1 = f1
        self.f2 = f2

     def go(self):
         if(self.f1.get_xp() > self.f2.get_xp()):
             print(f"the winner is{self.f1.name()}")
             del self.f2

         elif (self.f1.get_xp() < self.f2.get_xp()):
             print(f"the winner is({self.f2.name()})")
             del self.f1
         else:
             print(f"draw")    

fighter1 = fighter("john",10)
fighter2 = fighter("Abby",110)
Fight = fight(fighter1,fighter2)
fight.go()


    



