class Animal:
    alive = []
    def __init__(self: name,):
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def Herbivore(self: hide):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target):
        isinstance(target, Herbivore)
        if isinstance(target, Herbivore) and target.hidden == False:
            target.health -= 50

            if target.healt <= 0:
                Animal.alive.remove(target)

                if target in Animal.alive:
                    Animal.alive.remove(target)
