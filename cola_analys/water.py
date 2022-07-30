from liquid import Liquid
from substance import Substance


class Water(Liquid):
    ruClassName = "Вода"
    def info_water(self):
        return(f"\nЯ - {Substance.ruClassName}\nМоё агрегатное состояние - {Liquid.ruClassName}\nЯ - {Water.ruClassName}")