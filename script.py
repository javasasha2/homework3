# Базовий клас
class ТранспортнийЗасіб:
    def __init__(self, швидкість):
        self.швидкість = швидкість  # км/год

    def переміщення(self):
        return f"Рухається зі швидкістю {self.швидкість} км/год"


# Підклас Автомобіль
class Автомобіль(ТранспортнийЗасіб):
    def переміщення(self):
        return f"Автомобіль їде по дорозі зі швидкістю {self.швидкість} км/год"


# Підклас Потяг
class Потяг(ТранспортнийЗасіб):
    def переміщення(self):
        return f"Потяг рухається по рейках зі швидкістю {self.швидкість} км/год"


# Підклас Літак
class Літак(ТранспортнийЗасіб):
    def переміщення(self):
        return f"Літак летить у повітрі зі швидкістю {self.швидкість} км/год"


# Приклад використання
авто = Автомобіль(90)
потяг = Потяг(120)
літак = Літак(850)

print(авто.переміщення())
print(потяг.переміщення())
print(літак.переміщення())
