import os
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import CHROMEDRIVER_PATH
from trophie import Trophie, Guide

rarity_pattern = re.compile(r'\d{1,3}\.\d{1,2}')  # паттерн для поиска процентов игроков
link_match_with_ajax = re.compile(r'^https:\/\/www\.stratege\.ru\/ps4\/games\/.+\/trophies#args:ajax=1$')
link_match_without_ajax = re.compile(r'^https:\/\/www\.stratege\.ru\/ps4\/games\/.+\/trophies$')
borders = {  # ключ - класс рамки, значение - Описание на русском
    'tltstpl_border_platinum_trophies': 'Платиновый',
    'tltstpl_border_gold_trophies': 'Золотой',
    'tltstpl_border_silver_trophies': 'Серебряный',
    'tltstpl_border_bronze_trophies': 'Бронзовый'
}
trophy_list = []


def get_trophies(game='', out_link=''):
    # region Opening Browser
    link = "https://www.stratege.ru/ps4/games/{game}/trophies#args:ajax=1"  # ссылка, куда будем подставлять название игры
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    if out_link == '':
        browser.get(link.format(game=game))
    else:
        browser.get(out_link)
    time.sleep(5)  # т.к. страница медленно грузится
    page = browser.page_source
    browser.close()
    soup = BeautifulSoup(page, 'lxml')
    if 'К сожалению, такой игры на сайте не существует.' in soup.text:
        print('К сожалению, такой игры на сайте не существует. Попробуйте снова')
        return -1
    # endregion
    # region Parsing html
    for trophie in soup.find_all(attrs={'class': 'tltstpl_trophies'}):
        title = trophie.find(attrs={'class': 'tltstpl_tt_trops_title_box'}).text.strip()
        tag = trophie.find(attrs={'class': 'tltstpl_border_trophies'})
        difficult = borders[tag['class'][1]]
        rarity = float(
            rarity_pattern.search(trophie.find(attrs={'class': 'tltstpl_tt_trops_rarity'}).text.strip()).group(0))
        guides = []
        for slider_page in trophie.find_all(attrs={'class': 'tlhsltpl_slider_table_td'}):
            main_part = {}
            additions = {}
            index = 0
            for author_tag, guide_tag in zip(slider_page.find_all(attrs={'class': 'tlhsltpl_helps_header_autor'}),
                                             slider_page.find_all(attrs={'class': 'viewstgix_layer_find'})):
                author = str.join(' ', [el for el in author_tag.find('a')['title'].split()[1:]])
                guide_data = guide_tag.text.strip()
                for link in guide_tag.find_all('a'):
                    guide_data += '\n' + link.get('href')
                if index == 0:
                    main_part[author] = guide_data
                else:
                    additions[author] = guide_data
                index += 1
            guides.append(Guide(main_part, additions))
        trophy_list.append(Trophie(title, difficult, rarity, guides))
    return 0
    # endregion


def main_menu():
    while True:
        try:
            print(
                'Введите название игры с трофеями для PS4, \nпришлите ссылку на страницу с трофеями сайта stratege.ru \nили напишите "Выход" для выхода из программы. \nStratege.ru работает очень медленно!')
            choice = input()
            if link_match_with_ajax.match(choice) or link_match_without_ajax.match(choice):
                if get_trophies(choice) == 0:
                    choice2 = input('Вывести подсказки по всем трофеям? Да\нет\n')
                    if choice2.lower() == 'да':
                        print(str.join('', [str(el) for el in trophy_list]))
                    elif choice2.lower() == 'нет':
                        print(str.join('\n', [str(el.title) for el in trophy_list]))
                        choice3 = input('Введите название трофея из списка\n')
                        if choice3 in [troph.title for troph in trophy_list]:
                            print([troph for troph in trophy_list if troph.title == choice3][0])
                        else:
                            print(f'Такого трофея нет. Введите название полностью. Например "{trophy_list[0].title}"')
                    else:
                        print('Я вас не понимаю :(')
            elif choice.lower().strip() == 'выход':
                print("Пока!")
                exit(0)
            else:
                if get_trophies(str.join('_', choice.split())) == 0:
                    choice2 = input('Вывести подсказки по всем трофеям? Да\нет\n')
                    if choice2.lower() == 'да':
                        print(str.join('', [str(el) for el in trophy_list]))
                    elif choice2.lower() == 'нет':
                        print(str.join('\n', [str(el.title) for el in trophy_list]))
                        choice3 = input('Введите название трофея из списка\n')
                        if choice3 in [troph.title for troph in trophy_list]:
                            print([troph for troph in trophy_list if troph.title == choice3][0])
                        else:
                            print(f'Такого трофея нет. Введите название полностью. Например "{trophy_list[0].title}"')
                    else:
                        print('Я вас не понимаю :(')
            input()
            os.system('cls')
            trophy_list.clear()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main_menu()
