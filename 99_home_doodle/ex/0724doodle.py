class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r**2

    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)

won = Circle(3, 2, 4)
print(won.area())
print(won.circumference())