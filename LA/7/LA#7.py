class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

Honda = Car ("Honda" , "Black")
Ferrari = Car ("Ferrari" , "Red")
print("Original Brand and Color:",Honda.brand,Honda.color)
Honda.color = "Green"
print("Updated Brand and Color:",Honda.brand,Honda.color)
print("Updated Brand and Color:",Ferrari.brand,Ferrari.color)
