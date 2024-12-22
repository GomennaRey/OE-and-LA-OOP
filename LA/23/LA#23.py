class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character can absorb the energy of the environment turns into massive bomb!")
        return wrapper

Goku = AnimeCharacter("Goku", "Spirit Bomb!")
@Goku.introduce
def character_intro():
    print(f"I am {Goku.name} and I can use {Goku.ability}.")

character_intro()
