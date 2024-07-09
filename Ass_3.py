class Assignment:

  def __init__(self, Character ="Bittu", age = 20):
    self.Character = Character
    self.age = age

  def character(self, value):
    self.character = value

  def age(self, value):
    self.age = value
    
  def display(self):
    print(f"{self.Character} is {self.age} years old.")
   
a = Assignment() 
a.display()
b = Assignment("Divyansh","20")
b.display()
