


class Flavor_enhancers():
    ruClassName = "Усилители вкуса"

    def info_flavor_enhancers(self):
        return (f"Мы - {Flavor_enhancers.ruClassName}\nВ состав входят:\n{Sugar.ruClassName},"
                f"{Sugar_surrogate.ruClassName},{Caramel.ruClassName},{Phosphorus.ruClassName},{Natrium.ruClassName}\n"
                f"С нашей помощью вода получается с различными вкусами")
    def info_sostav(self):
        return f"{Sugar.ruClassName},{Phosphorus.ruClassName},{Sugar_surrogate.ruClassName},{Caramel.ruClassName}," \
               f"{Natrium.ruClassName},{Nature_flavors.ruClassName}"


class Sugar(Flavor_enhancers):
    ruClassName = "Сахар"


class Phosphorus(Flavor_enhancers):
    ruClassName = "Фосфорная кислота"

class Sugar_surrogate(Flavor_enhancers):
    ruClassName = "Заменитель сахара"


class Caramel(Flavor_enhancers):
    ruClassName = "Карамельный колер"


class Natrium(Flavor_enhancers):
    ruClassName = "Бензонат натрия"

class Nature_flavors(Flavor_enhancers):
    ruClassName = "Натуральные ароматизаторы"



