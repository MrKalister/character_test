"""Суперкрутая игра с заставкой."""

from random import randint
from typing import Optional, Tuple


DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    """Базовая модель персонажа."""
    RANGE_VALUE_ATTACK: Tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: Tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'

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
        return (
            f'{self.name} применил специальное умение - {self.SPECIAL_SKILL}.'
            f' Твоя {self.SPECIAL_SKILL} составляет {self.SPECIAL_BUFF} ед.'
        )

    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    """Класс персонажа - Warrior(Воитель)."""
    RANGE_VALUE_ATTACK: Tuple[int, int] = (3, 5)
    RANGE_VALUE_DEFENCE: Tuple[int, int] = (5, 10)
    SPECIAL_SKILL: str = 'Выносливость'
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    BRIEF_DESC_CHAR_CLASS: str = (
        'дерзкий воин ближнего боя. Сильный, выносливый и отважный'
    )


class Mage(Character):
    """Класс персонажа - Mage(Маг)."""
    RANGE_VALUE_ATTACK: Tuple[int, int] = (5, 10)
    RANGE_VALUE_DEFENCE: Tuple[int, int] = (-2, 2)
    SPECIAL_SKILL: str = 'Атака'
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    BRIEF_DESC_CHAR_CLASS: str = (
        'находчивый воин дальнего боя. Обладает высоким интеллектом'
    )


class Healer(Character):
    """Класс персонажа - Healer(Лекарь)."""
    RANGE_VALUE_ATTACK: Tuple[int, int] = (-3, -1)
    RANGE_VALUE_DEFENCE: Tuple[int, int] = (2, 5)
    SPECIAL_SKILL: str = 'Защита'
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    BRIEF_DESC_CHAR_CLASS: str = (
        'могущественный заклинатель. Черпает силы из природы, веры и духов'
    )


def start_training(char_class: Character) -> Optional[str]:
    """Тренировочная игра."""
    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или '
        'special — чтобы использовать свою суперсилу.'
    )
    print('Если не хочешь тренироваться, введи команду skip.')
    commands = {
        'attack': char_class.attack,
        'defence': char_class.defence,
        'special': char_class.special
    }
    cmd: Optional[str] = None
    while cmd != 'skip':
        cmd = input('Введи команду: ').lower()
        try:
            print(commands[cmd]())
        except KeyError:
            print('Убедитесь в правильности написания команды')
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Optional[Character]:
    """Функция выбора персонажа."""
    game_classes: dict = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer
    }
    approve_choice: Optional[str] = None

    while approve_choice != 'y':
        selected_class: str = input(
            'Выберите персонажа за которого будешь играть. '
            'Введите на английском языке: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: '
        ).lower()
        try:
            char_class: Character = game_classes[selected_class](char_name)
            print(char_class)
            approve_choice = input(
                'Нажми (Y), чтобы подтвердить выбор, '
                'или любую другую кнопку, '
                'чтобы выбрать другого персонажа '
            ).lower()
        except KeyError:
            print(
                'Такого персонажа еще не существует. '
                'Выберите из предложенных')
    return char_class


if __name__ == '__main__':
    from graphic_arts.start_game_banner import run_screensaver

    def main():
        run_screensaver()
        print('Приветствую тебя, искатель приключений!')
        print('Прежде чем начать игру...')
        char_name = input('...назови себя: ')
        if char_name == '':
            char_name = 'Неопознанный енот'
        print(
            f'Здравствуй, {char_name}! '
            f'Сейчас твоя выносливость — {DEFAULT_STAMINA}, '
            f'атака — {DEFAULT_ATTACK} и защита — {DEFAULT_DEFENCE}.'
        )
        print('Ты можешь выбрать один из трёх путей силы:')
        char_class = choice_char_class(char_name)
        print(start_training(char_class))

    main()
