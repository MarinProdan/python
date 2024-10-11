class CeleCislo:
    def __init__(self,cisla = []):
        self.cisla = cisla
    def je_prirozene(self):
        for cislo in self.cisla:
          if (cislo > 0 or cislo == 0):
            print(f"{cislo} je prirozene")
          else:
            print(f"{cislo} neni prirozene")

    def __str__(self):
        return str(self.cisla)
    def je_prvocislo(self):
      for i in range(2,int(self.cisla**0,5)+1):
        if(self.cisla%i==0):
          return True
        else:
          return False
      


cisla = CeleCislo([11, -1, 0, 5, 27, 29])
cisla.je_prirozene()
cisla.je_prvocislo()
print(cisla)
