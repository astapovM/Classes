from substance import Substance


class Liquid(Substance):
    ruClassName = "Жидкость"

    def info(self):
        """Аргумент density.в чем измеряется плотность жидкости"""

        print(f"Я - {Substance.ruClassName}")
        print(f"Я - {Liquid.ruClassName}")
        print(f"Моя плотность измеряется в {self}")


Liquid.info('кг/м³')



