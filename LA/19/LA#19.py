class Foods:
    def __init__(self , name, ingredients, recipe):
      self.name = name
      self.ingredients = ingredients
      self.recipe = recipe
    def __str__(self):
        return f"Ang paborito kong ingredients ay {self.name} , {self.ingredients} , {self.recipe} para sa aking Turon"
Turon_recipe = Turon ("Wrapper" , "Saging" , "Asukal")
Abodo_recipe = Foods ("Manok" , "Toyo" , "Suka")
Sinigang_recipe = Foods ("Baboy" , "Sinigang Mix" , "Sabaw" )
print(f'''Turon: {Turon_recipe.__name} ,
Adobo: {Adobo_recipe.__name} , 
Sinigang: {Sinigang_recipe.__name''')
