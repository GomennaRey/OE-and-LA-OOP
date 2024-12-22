class Hero():
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
  def describeHero(self):
      print(f"{self.name} has {self.hp} HP")
class Marksman(Hero):
  pass

miya = Marksman("miya" , 100)
miya.describeHero()
