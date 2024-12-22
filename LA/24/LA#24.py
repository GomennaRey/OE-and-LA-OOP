from abc import ABC, abstractmethod
class GameCharacter:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
class Warrior(GameCharacter):
    def attack(self):
        print("Balmond use Sweeper!")
        
class Mage(GameCharacter):
     def attack(self):
        print("Nana use Molina!")
        
class Archer(GameCharacter):
    def attack(self):
        print("Miya use Arrow Sweeper!")
        
class Heal(GameCharacter):
     def attack(self):
        print("Rafaela use Blessing!")

Balmond = Warrior("Balmond , Sweeper!")
Nana = Mage("Nana , Molina")
Miya = Archer("Miya , Arrow Sweep")
Rafaela = Heal ("Rafaela , Blessing!")

Balmond.attack()
Nana.attack()
Miya.attack()
Rafaela.attack()
