class Assignment:

  def __init__(self, Character ="Bittu", age = 20):
    self.Character = Character
    self.age = age
    print(f"{self.Character} is {self.age} years old.")
   
a = Assignment() 
b = Assignment("Divyansh","20")
