class Substance:
    ruClassName = "Вещество"

    def __init__(self, volume):
        self.volume = volume


class Liquid(Substance):
    ruClassName = "Жидкое вещество"

    def __init__(self, volume, name, density, temperature):
        super().__init__(volume)
        self.name = name
        self.density = density
        self.temperature = temperature

    def boil(self):
        """Действие: влияние температуры"""
        if self.temperature >= 100:
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я буду кипеть")
        elif self.temperature <= 0:
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я превращусь в лёд")
        else:
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я чисто на расслабоне,на чиле")



    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Liquid.ruClassName}")
        print(f"Мое название - {self.name}")
        print(f"Мой объем измеряется в  - {self.volume}")
        print(f"Моя плотность - {self.density}")


class Solid(Substance):
    ruClassName = "Твердое вещество"

    def __init__(self, volume, name, durability):
        super().__init__(volume)
        self.name = name
        self.durability = durability

    def write(self):
        return "записывать"

    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Solid.ruClassName}")
        print(f"Мое название - {self.name}")
        print(f"Мой объем измеряется в  - {self.volume}")
        print(f"Моя прочность - {self.durability}")
        print(f"Я могу совершать действие : {self.write()}")


class Gas(Substance):
    ruClassName = "Газообразное вещество"

    def __init__(self, volume, name, autoignition_temperature):
        super().__init__(volume)
        self.name = name
        self.autoignition_temperature = autoignition_temperature

    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Gas.ruClassName}")
        print(f"Мое название - {self.name}")
        print(f"Мой объем измеряется в  - {self.volume}")
        print(f"Моя температура самовозгорания - {self.autoignition_temperature}")


cola = Liquid("мл и литр", "Coca-Cola", "1040 кг\м³", 6)
cola.info()
water = Liquid("мл и литр", "Вода", "997 кг\м³", -1)
water.info()
soda = Liquid("мл и литр", "Напитки из Черноголовки", "1030 кг\м³",101)
soda.info()
print("#" * 25)
pencil = Solid("cм³", "Карандаш", "низкая")
pencil.info()
print("#" * 25)
crap = Gas("м³", "Пердеж", "650°C")
crap.info()
print("#" * 25)

cola.boil()
water.boil()
soda.boil()
