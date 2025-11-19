# col_5.py => 21 строка

words = re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", phrase.lower())
# как сюда подставить знаки . , - / ? ! : ; "" ''
# words = re.findall(r"[a-zA-Zа-яА-ЯёЁ?!/'".,-]+", phrase.lower()) => но так почему-то не работает (
