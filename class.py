class human:
    def __init__(self, fname, lname,age2):
        self.first_name = fname
        self.last_name =lname
        self.age = age2
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"
matej=print
h = human("John", "Doe",99)
matej(h.first_name,h.last_name,h.age)
