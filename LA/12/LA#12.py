class Toy:
  def __init__(self, name, price):
      self.name = name
      self.price = price
  def describeToy(self):
      print(f"{self.name} and its price {self.price}")

      super().__init__(name, price)
Toy_Class = Toy ("Toy Car" , "$300")
Toy_Class.describeToy()
