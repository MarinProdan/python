class person:
    alive = 0

    def __init__(self,h= "homeless"):
        person.alive += 1
        if(h in ["home","homeless","cottage","flat","house","villa","residance"]):
         self.habitation = h
        else:
           self.habitation = "homeless"

    def __del__(self):
        person.alive -= 1
    def get_alive(self):
        return person.alive  
    def get_habitation(self,):
        return self.habitation
    def set_habitation(self,h):
        if(h in ["home","homeless","cottage","flat","house","villa","residance"]):
            self.habitation = h
        else:
            self.habitation = "homeless"
    def __str__(self):
        return f"There alive {person.alive} people there.This person habitation status is {self.habitation}."
    
p,q,r=person("house"), person(), person("residance")  
del r 
print(p)
print(q)

