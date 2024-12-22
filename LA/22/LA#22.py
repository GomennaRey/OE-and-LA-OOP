class Party:
    def __init__(self,theme):
        self.theme = theme
    def __secret_dish(self):
        print(f"Secret Dish: Macarons for the {self.theme} Party!")
    def celebration(self):
        print(f"{self.theme} Foods: stick O, cupcake, ice cream")
        print("Special Dish: Chocolate fountain")
        self.__secret_dish()
       
Birthday_party = Party("Birthday")
Christmas_party = Party("Christmas")
Pool_party = Party("Pool")
Birthday_party.celebration()
Christmas_party.celebration()
Pool_party.celebration()
