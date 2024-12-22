class Turon:
    def __init__(self , wrapper, saging, asukal):
      self.wrapper = wrapper
      self.saging  = saging
      self.asukal = asukal
    def __str__(self):
        return f"Ang paborito kong ingredients ay {self.wrapper} , {self.saging} , {self.asukal} para sa aking Turon"
Turon_recipe = Turon ("1 Kilo Wrapper" , "Malaking Saging" , "Asukal")

print(Turon_recipe)
