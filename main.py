class Mercedes:
    def __init__(self, модель, двигатель, мошность, ускорение, max_скорость):
        self.модель = модель
        self.двигатель = двигатель
        self.мошность = мошность
        self.ускорение = ускорение
        self.max_скорость = max_скорость

    def info(self):
        print(f"Mersedes benz Модель {self.модель}")
        print(f"Двигатель {self.двигатель}")
        print(f"Мощность {self.мошность}")
        print(f"ускорение 0-100 km/h {self.ускорение}")
        print(f"Максимальная скорость {self.max_скорость}")

c = Mercedes("CLS-63 AMG-Class", "W218 M157 V8 BITURBO️😮‍💨", "2000 hp", "2.3 sec", "510 km/h")
c.info()

