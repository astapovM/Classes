class Flavor_enhancers:
    ruClassName = "Усилители вкуса"

    def info_flavor_enhancers(self):
        return (f"Мы - {Flavor_enhancers.ruClassName}\nВ состав входят:\n{Sugar.ruClassName},"
                f"{Sugar_surrogate.ruClassName},{Caramel.ruClassName},{Phosphorus.ruClassName},{Natrium.ruClassName}")


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


flavors=Flavor_enhancers()

print(flavors.info_flavor_enhancers())
