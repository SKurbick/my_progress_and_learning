import requests
from pprint import pprint #более красивый вывод принта (читабельный)

url = "https://akabab.github.io/superhero-api/api/all.json" # закрепили к переменной апи-адрес в формате json
resp = requests.get(url) #использовали метод "get" что бы получить информацию с данными для последующей работы

#создали три (пока) пустых словаря
hulk_intel = {}
captain_am_intel = {}
thanos_intel = {}

heroes = [hulk_intel, captain_am_intel, thanos_intel] # добавили переменные со словарями в список

#логика, которая используется в цикле будет искать нужным нам героев и добавлять их умения
# и навыки(powerstats) в пустые словари выше
for res in resp.json():
    if res['name'] == 'Thanos': #  ищет по ключу имя героя
        thanos_intel[res['name']] = res['powerstats']# выполняется действия если поиск в цикле нашёл нужного героя
                                                    # то есть создает в пустом словаре выше новое ключ значение с именем героя
                                                    #привязывая к имени героя(ключ) значение(словарь) со статистикой героя
    if res['name'] == 'Hulk':
        hulk_intel[res['name']] = res['powerstats']
    if res['name'] == 'Captain America':
        captain_am_intel[res['name']] = res['powerstats']

  #переменная в которой идёт сравнение(закрепляет автоматически самоее большее значение методом "max")
# из ключа "intelligence" (сравнивается интеллект)
max_intel = (max(hulk_intel['Hulk']['intelligence'], captain_am_intel['Captain America']['intelligence'],
                 thanos_intel['Thanos']['intelligence']))
#в цикле мы обращаемся к переменной с данными каждого героя что бы сравнить с данными max_intel и
# вывести сообщение о герое с большим интеллектом
for hero in heroes:
    for her in hero.items():# используем items...
        if her[1]['intelligence'] == max_intel:#... что бы можно было обратиться к данным по индексу
            pprint(f'{her[0]} have max intelligence: {max_intel}') #выводим сообщение с результатами используя f-строку


#программа, которая достает апи-данные в специальном json формате и сравнивает определенные их характеристики.
# в нашем примере он сравнивает интеллект определенных героев