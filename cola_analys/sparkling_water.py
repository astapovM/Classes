import flavor_enhancers as flavor
import package


class Substance:
    ruClassName = "Вещество"


class Liquid(Substance):
    ruClassName = "Жидкость"

    def __init__(self, temperature):
        self.temperature = temperature

    def boil(self):
        """Действие: влияние температуры"""
        if self.temperature >= 100:
            print(f"[INFO] При температуре {self.temperature}°C я буду кипеть.")
        elif self.temperature <= 0:
            print(f"[INFO] При температуре {self.temperature}°C я превращусь в лёд.")
        elif self.temperature in range(1, 21):
            print(f"[INFO] При температуре {self.temperature}°C я буду вкусным напитком.")
        else:
            print(f"[INFO] При температуре {self.temperature}°C я врядли буду вкусным напитком")


class Water(Liquid):
    ruClassName = "Вода"

    def info_water(self):
        return (
            f"\nЯ - {Substance.ruClassName}\nМоё агрегатное состояние - {Liquid.ruClassName}\nЯ - {Water.ruClassName}")


class Gas(Substance):
    ruClassName = "Газ"

    def __init__(self, pressure):
        self.pressure = pressure


class Sparkling_water(Water, Gas):
    ruClassName = "Газированная вода"

    def info_sparkling_water(self):
        return (f'Я - {Sparkling_water.ruClassName}\nПолучаюсь при смешивании {Gas.ruClassName} + {Water.ruClassName}')


class Cola(Sparkling_water):
    ruClassName = "Кока-Кола"

    def __init__(self, temperature, pressure):
        super().__init__(temperature)
        self.pressure = pressure

    def gas_pressure(self):
        """'Газировонность напитка'"""
        if self.pressure >= 2.5 and self.pressure <= 3.5:
            print(f"[INFO] Давление газа в {self.pressure} атм. идеально")
        elif self.pressure >= 4:
            print(f"[INFO] Давление газа в {self.pressure} атм. избыточно.Будьте осторожны при открытии упаковки")
        else:
            print(f"[INFO] Давление газа в {self.pressure} атм. недостаточно.Продукт испорчен")

    def sostav(self):
        print(f"Я - {self.ruClassName}.Я состою из различных {Substance.ruClassName[0:-1]},таких как :\n"
              f"{Water.ruClassName},{flavor.Flavor_enhancers.info_sostav('self')}")


cola = Cola(11, 3)
print(cola.info_water())
print(cola.info_sparkling_water())
cola.sostav()
cola.boil()
cola.gas_pressure()
print("#" * 30)
sprite = Cola(21, 5)
sprite.ruClassName = "Спрайт"
print(sprite.info_water())
print(sprite.info_sparkling_water())
sprite.sostav()
sprite.boil()
sprite.gas_pressure()
print("#" * 30)

fanta = Cola(-1, 1)
fanta.ruClassName = "Фанта"
print(fanta.info_water())
print(fanta.info_sparkling_water())
fanta.sostav()
fanta.boil()
fanta.gas_pressure()
print(package.Package.ruClassName)
print(package.Package.banka)
