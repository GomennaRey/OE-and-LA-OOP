class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def player_atk(self , enemy_object):
        enemy_object.health = enemy_object.health - self.attack_power
Nemo = Player("Nemo" , 1000 , 50)
Dori = Player("Dori" , 500, 50)
while Nemo.health > 0 and Dori.health > 0:
    Nemo.player_atk(Dori)
    Dori.player_atk(Nemo)

    if Nemo.health > Dori.health:
        print(f"{Nemo.name} , {Nemo.health} Hp left")
    if Dori.health > Nemo.health:
        print(f"{Dpri.name} , {Dori.health} Hp left")
if Nemo.health > Dori.health:
    print("Nemo Wins")
else:
    print("Dori Wins")
print(Nemo.name , Nemo.health , Nemo.attack_power)
print(DOri.name , Dori.health , Dori.attack_power)
