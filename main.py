class Mercedes:
    def __init__(self, модель, двигатель, мошность, ускорение, мах_скорость):
        self.модель = модель
        self.двигатель = двигатель
        self.мошность = мошность
        self.ускорение = ускорение
        self.max_скорость = мах_скорость

    def info(self):
        print(f"Mersedes benz Модель {self.модель}")
        print(f"Двигатель {self.двигатель}")
        print(f"Мощность {self.мошность}")
        print(f"ускорение 0-100 km/h {self.ускорение}")
        print(f"Максимальная скорость {self.max_скорость}")

c = Mercedes("CLS-63 AMG-Class", "W218 M157 V8 BITURBO️😮‍💨", "2000 hp", "2.3 sec", "510 km/h")
c.info()


class MercedesAMG(Mercedes):
    def __init__(self, модель, двигатель, мошность, ускорение, max_скорость, дополнительная_особенность):
        super().__init__(модель, двигатель, мошность, ускорение, max_скорость)
        self.дополнительная_особенность = дополнительная_особенность

    def display_info(self):
        super().display_info()
        print(f"Дополнительная особенность: {self.дополнительная_особенность}")


c = MercedesAMG("CLS-63 AMG-Class", "W218 M157 V8 BITURBO️😮‍💨", "2000 hp", "2.3 sec", "510 km/h", "Специальная аэродинамическая установка")
c.display_info()

class BMW(Mercedes):
    def __init__(self, модель, двигатель, мошность, ускорение, max_скорость):
        super().__init__(модель, двигатель, мошность, ускорение, max_скорость)

bmw = BMW("BMW M5", "S63 V8", "600 hp", "3.4 sec", "305 km/h")
bmw.display_info()