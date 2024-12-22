class Appliance:
    def __init__(self, brand, model, info):
      self.brand = brand
      self.model = model
      self.info = self.info
    def describeInfo(self):
        printf("{self.brand}: the brand of the appliance, {self.mode}: the model of the appliance")
class WashingMachine(Appliance):
    def __init__(self, brand, model, info):
        Appliance.__init__(self, brand, model, info)
        self.info()
        print(f"{self.name}: {self,brand}")
class Refrigerator(Appliance):
    def __init__(self, brand, model, info):
        Appliance.__init__(self, brand, model, info)
        self.info()
class Microwave(Appliance):
    def __init__(self, brand , model):
        super().__init__(brand, model)

Washing = WashingMachine("Hanabishi" , "F6WV709P1")
Ref = Refrigerator("Fujidenzo" , "INR-83 HS")
Mic = Microwave("Hanabishi" , "HMO20G")

for x in [Washing, Ref, Mic]:
    x.describeInfo()
