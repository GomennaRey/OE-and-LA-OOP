class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} with {self.attack_power} damage")
        print(f"{target.name} has only {target.health} hp left")
        if target.health <= 0:
            print(f"The {target.name} is already defeated")
        
        
Goku = Player("Goku", 50, 8)
Vegeta = Player("Charmander", 60, 6)

Goku.attack(Charmander)
Charmander.attack(Goku)

while Goku.health > 0 and Vegeta.health > 0:
    Goku.attack(Vegeta)
    if Vegeta.health <= 0:
        print(f"{Goku.name} wins!")
        break
    Vegeta.attack(Goku)
    if Goku.health <= 0:
        print(f"{Vegeta.name} wins!")
        break
