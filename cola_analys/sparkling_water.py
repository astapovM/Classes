class Substance:
    ruClassName = "Вещество"


class Liquid(Substance):
    ruClassName = "Жидкость"

class Water(Liquid):
    ruClassName = "Вода"
    def info_water(self):
        return(f"\nЯ - {Substance.ruClassName}\nМоё агрегатное состояние - {Liquid.ruClassName}\nЯ - {Water.ruClassName}")

class Gas(Substance):
    ruClassName = "Газ"


class Sparkling_water(Water, Gas):
    ruClassName = "Газированная вода"
    def info_sparkling_water(self):
        return(f'Я-{Sparkling_water.ruClassName}\nПолучаюсь при смешивании {Gas.ruClassName} + {Water.ruClassName}')

water=Sparkling_water()

print(water.info_water())
print(water.info_sparkling_water())













