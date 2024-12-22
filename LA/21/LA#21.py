class Adobo:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat
        self._dryseason = dry_season
        self.__wetseason = wet_season 
        
    def __str__(self):
        return f"Ang adobo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
        
    def may_carrot_ba(self):
        return self.__wetseason
        
    def set_carrot(self, bagong_value):
        self.__wetseason = bagong_value
    
adowbong_dry = Adowo("chicken", "water", "asin")
adowbow2 = Adobo("baka", "watir" , "tuyo")
adowbo3 = Adobo("Pork", "water" , "Onyon")
adowbong_dry.set_carrot("new carrot 1")
adowbow2.set_carrot("new carrot 2")
adowbo3.set_carrot("new carrot 3")
print(adowbong_dry.may_carrot_ba())
print(adowbow2.may_carrot_ba())
print(adowbo3.may_carrot_ba())
