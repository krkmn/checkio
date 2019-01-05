'''
Two armies battling eachother,
each army can have soldiers with warrior class and knight class
'''
class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self._is_alive = True

    @property
    def is_alive(self):
        if self.health <= 0:
            self._is_alive = False
        return self._is_alive


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

    pass


def fight(unit_1, unit_2):
    while (unit_2.is_alive and unit_1.is_alive):
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
        else:
            return True
    return False


class Army:

    def __init__(self):

        self.units = []
        self._is_alive = True

    def add_units(self, unit, amount):

        for i in range(amount):
            self.units.append(unit())

    @property
    def is_alive(self):
        if any([unit.is_alive for unit in self.units]):
            self._is_alive = True
        else:
            self._is_alive = False

        return self._is_alive


class Battle:

    def __init__(self):
        self.global_fight = fight

    def fight(self, army_1, army_2):

        while army_1.is_alive and army_2.is_alive:
            units_1_alive = [soldier.is_alive for soldier in army_1.units]
            units_2_alive = [soldier.is_alive for soldier in army_2.units]
            soldier_1 = army_1.units[units_1_alive.index(True)]
            soldier_2 = army_2.units[units_2_alive.index(True)]
            self.global_fight(soldier_1, soldier_2)

        if army_1.is_alive:
            return True

        return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")