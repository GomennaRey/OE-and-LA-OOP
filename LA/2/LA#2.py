class character:
    def __init__(self, name, hero_type):
        self.name = name
        self.hero_type = hero_type

hero = character("Moskov" , "Marksman")
print(hero.hero_type , hero.name)
