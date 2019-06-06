import re

text = input("Введите текст : ");


while(True):
    try:
        key = input("Введите ключевое слово: ")
        break
    except:
        print("Введён некоректный ключ")

alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alpha2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

result = ""
x = 0
for a in text:
    if re.search(r"[0-9]", a):
        result += a
    else:
        if a == " ":
            result += " "
        else:
            if re.search(r"[А-Я]", a):
                alpha2 += alpha2[(alpha2.index(a) + alpha.index(key[x])) % len(alpha2)]
            else:
                result += alpha[(alpha.index(a) + alpha.index(key[x])) % len(alpha)]
            if x == len(key) - 1:
                x = 0
            else:
                x += 1

print("Result: " + result)