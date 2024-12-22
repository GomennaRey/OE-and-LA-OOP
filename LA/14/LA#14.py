class Spiderman:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def describeSpiderman():
      print(f"{self.name.lower()} , {self.age}")

class Tobey (Spiderman):
  def __init__(self, name, age, movietitle):
      super().__init__(name, movietitle)
      self.movietitle = movietitle
Spidey = Tobey ("Tobey" , "27" , "No Way Home")
print(f"Name:{Spidey.name.upper()} , {Spidey.movietitle}")
class Andrew (Spiderman):
  def __init__(self, name, age, movietitle):
      super().__init__(name, movietitle)
      self.movietitle = movietitle
Spide = Andrew ("Andrew" , "17" , "The Amazing SpiderMan")
print(f"Name:{Spidey.name.upper()} , {Spidey.movietitle}")
class Tom (Spiderman):
  def __init__(self, name, age, movietitle):
      super().__init__(name, movietitle)
      self.movietitle = movietitle
Spid = Tom ("Tom" , "20" , "Home Coming")
print(f"Name:{Spidey.name.upper()} , {Spidey.movietitle}")
