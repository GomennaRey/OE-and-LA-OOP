class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return "My honda car"
my_car = Car ("Honda")
#print(my_car)
del my_car
