import collections
import random

# Эмоджи из паст по популярности
w = " ️\n-,.;:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890!?"
with open("base.txt", "r") as f:
    l = list(f.read())
    c = collections.Counter()
    for i in l:
        if not i in w:
            c[i] += 1
emj_top = ""
for i, vol in c.most_common():
    emj_top += vol * i

emj_top = list(emj_top)
random.shuffle(emj_top)

# Текст для пасты
text = '''
Бу, блять! Просыпайтесь нахуй
(Let's go!)
Головы сияют на моей едкой катание
Голоса этих ублюдков
По пятам бегут за нами
Погруженный в Изанами
Все колеса под глазами
Её взгляд убьёт любого
Её взгляд убьёт цунами
'''.replace("\n", "", 1)

# Веселые эмоджи, которые я нашел
emjs = list(
    "🔪❤🖤🖤😫😎😒😔😭😨😰🤤😢😷😳😵😠🙄🙄🙄😡😥😖🤐😤😓😱🤕😈👿👿😪🤒👻💀💩🙊👺👺👹😿👏🖕💪👀🙇🤡💔💔💓💖💗💘💟🌚🔞🆘🔥🔥⛔🐔🐓🥃🍺🍻🎃🎰💉💣💰💎🗿"
)

space = True


### Не нужны пробелы? Раскоментить некст строку
# space = False


def get_emj():
    # Исчем смайл
    while 1:
        # 65% на из топа
        if random.randint(0, 100) >= 35:
            emj = random.choice(emj_top)
        # 35% на рандомной
        else:
            emj = random.choice(emjs)
        if not (emj in emj_last[-5:]):
            break
    # 1% на дабл смайл
    if random.randint(0, 100) > 99:
        if random.randint(0, 100) > 60:
            emj += random.choice(emjs)
        else:
            emj *= 2
    emj_last.pop(0)
    emj_last.append(emj)
    return emj


def sp(emj, new_text, enter=False):
    # Рандомим пробелы после и перед смайлом
    global space
    if space:
        if enter:
            return random.choice(["", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]) + emj + "\n"
        else:
            if " " in new_text[-3:]:
                return emj + random.choice(["", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ])
            else:
                return random.choice(["", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]) + emj + random.choice(
                    ["", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ])
    else:
        return emj


new_text = ""
emj_last = list("123456")
for i in text:
    out = i
    if i == " ":
        # 90% на эможди если пробел
        if random.randint(0, 100) >= 10:
            emj = get_emj()
            out = sp(emj, new_text)

    elif i == "\n":
        # 95% на эможди если пробел
        if random.randint(0, 100) >= 5 or not space:
            emj = get_emj()
            out = sp(emj, new_text, enter=True)

    elif i == "," or i == ".":
        # Запятые/Точки 70% смайл
        if random.randint(0, 100) >= 30 or not space:
            emj = get_emj()
            out = sp(emj, new_text)

    new_text += out

# Вывод
print(new_text)
