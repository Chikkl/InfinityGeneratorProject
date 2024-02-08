from random import randint, choice


class Unit():
    special_skills = ['Призыв воинов', 'Щит на свою армию', 'Боевая ярость', 'Аннигиляция']

    def __init__(self, id:int, health:int, mana_pull:int, damage:int, defence:int, special_skill:str) -> None:
        self.character_stats = [id, health, mana_pull, damage, defence, special_skill]
    
    def __repr__(self) -> dict:
        return self.character_stats
    
    @classmethod
    def generate_captain_skill(cls) -> list:
        special_skill = choice(cls.special_skills)
        return special_skill


class Warior(Unit):
    def __init__(self, id:int = id, health:int = randint(100, 200), mana_pull:int = 0,
                         damage:int = randint(10, 100), defence:int = randint(10, 100), special_skill:str = False) -> None:
        super().__init__(id, health, mana_pull, damage, defence, special_skill)

class Archer(Unit):
    def __init__(self, id:int = id, health:int = randint(100, 150), mana_pull:int = 0,
                 damage:int = randint(50, 150), defence:int = randint(10, 50), special_skill:str = False) -> None:
        super().__init__(id, health, mana_pull, damage, defence, special_skill)

class WizardHealer(Unit):
    def __init__(self, id:int = id, health:int = randint(50, 100), mana_pull:int = 0,
                 damage:int = randint(10, 50), defence:int = randint(10, 30), special_skill:str = False) -> None:
        super().__init__(id, health, mana_pull, damage, defence, special_skill)

class Captain(Unit):
    def __init__(self, id: int = randint(0, 5), health: int = randint(200, 500), mana_pull: int = 0, damage: int = randint(100, 300), 
                 defence: int = randint(150, 250), special_skill: str = False) -> None:
        super().__init__(id, health, mana_pull, damage, defence, special_skill = super().generate_captain_skill())

class UnitGenerator():
    '''Данный класс отвечает за создание юнита по передаваемому в него "id". 
        На вход объекту класса должно передаваться целочисленное число от 0 до 100.000 и
        в зависимости от процентного соотношения, вы получите уникального юнита.'''
    def __init__(self, id: int) -> None:
        self.id = id

    def generate_unit_by_id(self) -> list:
        '''Функция генерации юнита по передаваемому "id".'''  
        if 5 <= self.id <= 10:                                            #крестьянин
            generated_unit = Unit(id=self.id, health=randint(1, 10), mana_pull=0, damage=randint(0, 5), defence=randint(0, 5), special_skill=None)
            return generated_unit
        elif 10 < self.id <= 49_999:                                          #воин
            return Warior(self.id)
        elif 49_999 < self.id <= 79_999:                                         #лучник
            return Archer(self.id)
        elif 79_999 < self.id <= 99_999:                                         #маг
            return WizardHealer(self.id)
        else:
            return Captain(self.id)

