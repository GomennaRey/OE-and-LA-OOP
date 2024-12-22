class TekkenCharacter:
    def __init__(self, name , ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def amazing():
            print("Introducing...")
            func()
            print("This Character is Amazing!")
        return amazing
"""class Nina(TekkenCharacter):
    def attack(self):
        print("Fatal Judgement")
    def character_info(self):
        print(f"I am {self.name} and I can use {self.ability}")"""
Tekken = TekkenCharacter("Nina" , "Fatal Judgement")
@Tekken.introduce
def character_intro():
    print(f"I am {Tekken.name} and I can use {Tekken.ability}")
character_intro()
