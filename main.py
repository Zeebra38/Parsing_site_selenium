import time
import re
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import CHROMEDRIVER_PATH #Путь к ChromeDriver
from bs4 import BeautifulSoup
from trophie import Trophie, guide
rarity_pattern = re.compile(r'\d{1,3}[.]\d{1,2}') #паттерн для поиска процентов игроков
borders = { # ключ - класс рамки, значение - Описание на русском
    'tltstpl_border_platinum_trophies': 'Платиновый',
    'tltstpl_border_gold_trophies': 'Золотой',
    'tltstpl_border_silver_trophies': 'Серебряный',
    'tltstpl_border_bronze_trophies': 'Бронзовый'
}
trophy_list = []
# region Opening Browser
# options = Options()
# options.headless = True
# browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
# browser.get('https://www.stratege.ru/ps4/games/hollow_knight/trophies#args:ajax=1')
# time.sleep(5)  # т.к. страница медленно грузится
# page = browser.page_source
# soup = BeautifulSoup(page, 'lxml')
# browser.close()
# with open('index.html', 'w') as f:
#     f.write(str(soup))
# endregion
# region Parsing html
with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
for trophie in soup.find_all(attrs={'class': 'tltstpl_trophies'}):
    title = trophie.find(attrs={'class': 'tltstpl_tt_trops_title_box'}).text.strip()
    tag = trophie.find(attrs={'class': 'tltstpl_border_trophies'})
    difficult = borders[tag['class'][1]]
    rarity = float(rarity_pattern.search(trophie.find(attrs={'class': 'tltstpl_tt_trops_rarity'}).text.strip()).group(0))
    for slider_page in help_list.find_all(attrs={'class':'tlhsltpl_slider_table_td'}):
        help_list = trophie.find(attrs={'class': 'tlhsltpl_helps_body'})
        for guide in help_list.find_all(attrs={'class':'tlhsltpl_helps_info_helps'}):
            author_tag = guide.find(attrs={'class':'tlhsltpl_helps_header_autor'})
            author = str.join(' ', [el for el in author_tag.find('a')['title'].split()[1:]])
            help_info = guide.find(attrs={'class': 'viewstgix_layer_find'})
            rez = help_info.text.strip('\t')
            for link in help_info.find_all('a'):
                rez += link.get('href')
            print(rez)
        for guide_add in help_list.find_all(attrs={'class':'tlhsltpl_add_helps_header'}):
            author_tag = guide_add.find(attrs={'class': 'tlhsltpl_helps_header_autor'})
            author = str.join(' ', [el for el in author_tag.find('a')['title'].split()[1:]])
            help_info = guide_add.find(attrs={'class': 'viewstgix_layer_find'})
            rez = help_info.text.strip('\t')
            for link in help_info.find_all('a'):
                rez += link.get('href')
            print(rez)


        #tlhsltpl_helps_text_helps viewstgix_layer_find
        #tlhsltpl_add_helps_text viewstgix_layer_find
        # for child in author_tag.children:
        #     print(type(child))
        #     print(child)
            #print(child.attrs)
            # if 'Пользователь' in child.title:
            #     print(child.title)
        break
    trophy_list.append(Trophie(title, difficult, rarity))
    #print(f'{title}\n{difficult}')
# print(str.join('', trophy_list))x
#print(trophy_list)
# endregion
