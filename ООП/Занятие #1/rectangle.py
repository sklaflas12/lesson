class Rectangle:
    def __init__(self,height,width) -> None:
        self.height = height
        self.width = width


    def Area(self):
        return self.height * self.width

    def Perimeter(self):
        return (self.height + self.width) * 2

    def Diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5
