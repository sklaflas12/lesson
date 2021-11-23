class Soda:
    def __init__(self, ingridient = ""):
        self.ingridient = ingridient
    

    def show_my_drink(self):
        if self.ingridient:
            print(f"Газировка и {self.ingridient}")
        else:
            print('Обычная газировка')


soda = Soda()
soda.show_my_drink()