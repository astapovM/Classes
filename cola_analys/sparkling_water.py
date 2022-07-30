from gas import Gas
from water import Water


class Sparkling_water(Water, Gas):
    ruClassName = "Газированная вода"
    def info_sparkling_water(self):
        return(f'Я-{Sparkling_water.ruClassName}\nПолучаюсь при смешивании {Gas.ruClassName} + {Water.ruClassName}')









