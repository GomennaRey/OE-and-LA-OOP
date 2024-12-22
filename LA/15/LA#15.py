class Dog:
  def __init__(self, name , animal_sound):
    self.name = name
    self.animal_sound = animal_sound
  def describeAnimal(self):
      print(f"{self.name}: {animal_sound}")
class Cat:
  def __init__(self , name , animal_sound):
    self.name = name
    self.animal_sound = animal_sound
  def describeAnimal(self):
     print(f"{self.name}: {animal_sound}")
class Bird:
  def __init__(self , name , animal_sound):
    self.name = name
    self.animal_sound = animal_sound
  def describeAnimal(self):
     print(f"{self.name}: {animal_sound}")
class Fish:
  def __init__(self , name , animal_sound):
    self.name = name
    self.animal_sound = animal_sound
  def describeAnimal(self):
     print(f"{self.name}: {animal_sound}")

Animal1 = Dog ("Garp D. Blackie" , "Bark!")
Animal2 = Cat ("Portugal D. Garfield" , "Meow!")
Animal3 = Bird ("Monkey D. Birdie" , "Chirp!")
Animal4 = Fish ("Gol D. Fish" , "...")

for Animal in [Animal1, Animal2, Animal3, Animal4]:
  Animal.describeAnimal()
