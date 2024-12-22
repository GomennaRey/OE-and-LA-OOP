class character:
    def __init__(self, name, hero_type):
        self.name = name
        self.hero_type = hero_type

    def describe(self):
        print(f"{self.name} is a {self.hero_type} hero")

hero = character("Moskov" , "Marksman")
hero.describe()
