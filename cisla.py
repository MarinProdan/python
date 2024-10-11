class CeleCislo:
    def __init__(self,cislo):
        self.cislo = cislo
    def je_prirozene(self):
          if (self.cislo > 0 or self.cislo==0):
            return True
          return False  
    
    def je_prvocislo(self):
      if self.cislo < 0:
        return False
      for i in range(2,int(self.cislo**0.5)+1):
        if self.cislo%i==0:
          return False
      return True
        
    def __str__(self):
      prirozene_text = "je" if self.je_prirozene() else "není"
      prvocislo_text = "je" if self.je_prvocislo() else "není"

      return f"Číslo {self.cislo} {prirozene_text} přirozené a {prvocislo_text} prvočíslo."

cisla = [-11, -1, 0, 5, 27, 29]
for cislo in cisla:
    cislo = CeleCislo(cislo)
    print(cislo)



