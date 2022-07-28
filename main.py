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
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я буду кипеть.")
        elif self.temperature <= 0:
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я превращусь в лёд.")
        else:
            print(f"[INFO:{self.name}] При температуре {self.temperature}°C я чисто на расслабоне,на чиле.")

    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Liquid.ruClassName}.")
        print(f"Мое название - {self.name}.")
        print(f"Мой объем измеряется в  - {self.volume}.")
        print(f"Моя плотность - {self.density}.")


class Solid(Substance):
    ruClassName = "Твердое вещество"

    def __init__(self, volume, name, durability, ink):
        super().__init__(volume)
        self.name = name
        self.durability = durability
        self.ink = ink

    def write(self):
        if self.ink > 0:
            print(f"[INFO: {self.name}].Во мне есть {pen.ink}% чернил.Я могу писать.")
        if self.ink < 0:
            print(f"[INFO: {self.name}].Я могу писать.")
        if self.ink == 0:
            print(f"[INFO: {self.name}].Во мне не осталось чернил. Я не могу писать.")

    def rewind(self):
        print(f"[INFO: {self.name}]. Могу перематывать кассету,экономя батарейки в плеере")

    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Solid.ruClassName}.")
        print(f"Мое название - {self.name}.")
        print(f"Мой объем измеряется в  - {self.volume}.")
        print(f"Моя прочность - {self.durability}.")


class Gas(Substance):
    ruClassName = "Газообразное вещество"

    def __init__(self, volume, name, autoignition_temperature):
        super().__init__(volume)
        self.name = name
        self.autoignition_temperature = autoignition_temperature

    def info(self):
        print(f"Я - {Substance.ruClassName}")
        print(f"Чтобы быть более точным: Я - {Gas.ruClassName}.")
        print(f"Мое название - {self.name}.")
        print(f"Мой объем измеряется в  - {self.volume}.")
        print(f"Моя температура самовозгорания - {self.autoignition_temperature}.")



cola = Liquid("миллилитрах", "'Coca-Cola'", "1040 кг\м³", 6)
cola.info()

print("#" * 25)
water = Liquid("миллилитрах", "'Вода'", "997 кг\м³", -1)
water.info()
vodka=Liquid()
print("#" * 25)
soda = Liquid("миллилитрах", "'Напитки из Черноголовки'", "1030 кг\м³", 101)
soda.info()

print("#" * 25)
pencil = Solid("cм³", "'Карандаш'", "низкая", -1)
pencil.info()

pen = Solid("cм³", "'Ручка'", "низкая", 15)

pen.info()
print("#" * 25)
crap = Gas("м³", "'Пердеж'", "650°C")
crap.info()
print("#" * 25)

# cola.boil()
# water.boil()
# soda.boil()
# pencil.rewind()
# pencil.write()
# pen.write()
# pen.rewind()
sostoyanie = {"жидкое": Liquid,
              "твердое": Solid,
              "газообразное": Gas
              }
# def anketa():
while True:
    print("Введите тип вещества: жидкое, твердое, газообразное")
    substance = input(">>>")

    if substance in sostoyanie:
        break
    else:
        continue
if substance == "жидкое":
    substance=Liquid
    print("Введите в чем измеряется мой объем: ")
    volume = input(">>>")

    print("Введите название вещества:")
    name = input(">>>")
    print("Моя плотность равна : кг\м³")
    density = input(">>>")
    print("Моя температура сейчас: ")
    temperature = input(">>>")
    new_liquid_ex = substance(volume, name, density + ' ' + 'кг\м³', int(temperature))
    new_liquid_ex.info()
    new_liquid_ex.boil()
elif substance == "твердое":
        substance = Solid


else:
    substance = Gas


