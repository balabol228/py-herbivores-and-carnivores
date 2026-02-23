class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}}}"

    def die(self) -> str:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        isinstance(target, Herbivore)
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.healt <= 0 and target in Animal.alive:
                Animal.alive.remove(target)
