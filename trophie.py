class Trophie:
    def __init__(self, title: str, difficult: str, rarity: float, help_info: dict = {}):
        self.title = title
        self.difficult = difficult
        self.rarity = rarity
        self.help_info = help_info

    def __str__(self):
        rez = ''
        if len(self.help_info) != 0:
            for item in self.help_info.items():
                rez += f'Подказка от {item[0]}:\n{item[1]}\n'
        return f'{self.difficult} трофей {self.title}.\nЕсть у {self.rarity} игроков.\n{rez if rez != "" else "Подсказок нет"}'

    def __repr__(self):
        rez = ''
        if len(self.help_info) != 0:
            for item in self.help_info.items():
                rez += f'Подказка от {item[0]}:\n{item[1]}\n'
        return f'{self.difficult} трофей {self.title}.\nЕсть у {self.rarity} игроков.\n{rez if rez != "" else "Подсказок нет"}'

class guide:
    def __init__(self, main_part: dict, additions: dict):
        self.main_part = main_part
        self.additions = additions

    def __str__(self):
        rez = ''
        for key, value in self.additions.items():
            rez += f'Дополнение от {key}: \n{value}'
        return f'Подсказка от {list(self.main_part.keys())[0]}: \n{self.main_part[list(self.main_part.keys())[0]]}.\nДополнения к подсказке:{rez} '

    def __repr__(self):
        rez = ''
        for key, value in self.additions.items():
            rez += f'Дополнение от {key}: \n{value}'
        return f'Подсказка от {list(self.main_part.keys())[0]}: \n{self.main_part[list(self.main_part.keys())[0]]}.\nДополнения к подсказке:{rez} '
