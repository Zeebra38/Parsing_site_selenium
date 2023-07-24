class Guide:
    def __init__(self, main_part: dict = {}, additions: dict = {}):
        self.main_part = main_part
        self.additions = additions

    def __str__(self):
        if len(self.additions.items()) > 0:
            rez = ''
            for key, value in self.additions.items():
                rez += f'\nДополнение от {key}: \n{value.strip()}\n'
            return f'Подсказка от {list(self.main_part.keys())[0]}: \n{self.main_part[list(self.main_part.keys())[0]]}.\nДополнения к подсказке:{rez}'
        else:
            return 'Подсказок нет'

    def __repr__(self):
        if len(self.additions.items()) > 0:
            rez = ''
            for key, value in self.additions.items():
                rez += f'\nДополнение от {key}: \n{value.strip()}\n'
            return f'Подсказка от {list(self.main_part.keys())[0]}: \n{self.main_part[list(self.main_part.keys())[0]]}.\nДополнения к подсказке:{rez}'
        else:
            return 'Подсказок нет'


class Trophie:
    def __init__(self, title: str, difficult: str, rarity: float, cur_guide: list[Guide]):
        self.title = title
        self.difficult = difficult
        self.rarity = rarity
        self.cur_guide = cur_guide

    def __str__(self):
        return f'{self.difficult} трофей {self.title}.\nЕсть у {self.rarity}% игроков.\n{str.join(" ", [str(el) for el in self.cur_guide])}\n'

    def __repr__(self):
        return f'{self.difficult} трофей {self.title}.\nЕсть у {self.rarity}% игроков.\n{str.join(" ", [str(el) for el in self.cur_guide])}\n'
