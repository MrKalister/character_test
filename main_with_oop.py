"""Суперкрутая игра с заставкой."""

from random import randint
from typing import Optional


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name) -> None:
        self.name = name

    def attack(self) -> str:
        """Метод атаки."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {value_attack}.'

    def defence(self) -> str:
        """Метод защиты."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона.'

    def special(self) -> str:
        """Метод специального умения."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL}{self.SPECIAL_BUFF}"')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')


class Mage(Character):
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')


class Healer(Character):
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')


def start_training(char_class: Character) -> Optional[str]:
    """Тренировочная игра."""
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    commands = {
        'attack': char_class.attack,
        'defence': char_class.defence,
        'special': char_class.special
    }
    cmd: str = input('Введи команду: ').lower()
    while cmd != 'skip':
        if cmd in commands:
            print(commands[cmd]())
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    game_classes = {
        'warior': Warrior,
        'mage': Mage,
        'healer': Healer
    }
    approve_choice: Optional[str] = None

    while approve_choice != 'y':
        selected_class = input(
            'Введи название персонажа, '
            'за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: '
        ).lower()
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    warrior = Warrior('Кодослав')
    print(warrior)
    print(warrior.attack())
