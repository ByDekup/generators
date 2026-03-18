import secrets as r, os
from pyperclip import copy
from eztools import SPEC_CHARS, LETTERS as ascii_letters
import pather

while True:
    qual = input("Введите кол-во символов в пароле (до 20, 20 самый надежный): ")
    if qual.isdigit(): qual=int(qual); break
    else: print("Введите только число от 1 до 20!")
    if qual > 20: print("Слишком много!")
    elif qual < 1: print("Слишком мало!")
    else: break
br = True
while True:
    specs=list(SPEC_CHARS) 
    p = []
    symbol = [*ascii_letters, *list(range(0, 10))]
    exclude=input(f'Какие символы исключить? ("all" если все, enter если никакие), вот они по умолчанию {" ".join(specs)}\n').lower()
    if exclude=="all": specs=[]
    elif exclude=="": specs=specs
    else:
        for char in exclude:
            try:
                specs.remove(char)
            except ValueError: continue
    print(f"Разрешенные вами символы: {" ".join(specs)}")
    symbol+=specs
    password = "".join(str(r.choice(symbol)) for _ in range(qual))
    print(password+" (скопировано в буфер обмена)")
    copy(password)
    wr = input("Написать пароль в текстовый файл? (Y/N): ").lower().strip()
    path = pather.get_exe(__file__) + "\\data\\python_logs.txt"
    if "y" in wr:
        if not os.path.exists(path): os.makedirs(os.path.dirname(path))
        with open(path, "a", encoding="utf-8") as pw:
            name = input("Название пароля: ")
            pw.write(f"{name}: {password}\n\n")
            print("Пароль внесён!")
            break
    elif "n" in wr: print("")
    else:
        print("Инвалидные данные, использую данные по-умолчанию (N)")
        br=True
        wr = "n"
    re = input("Перегенирировать пароль? (Y/N): ").lower().strip()
    if "n" in re: print("Всё прошло успешно!"); br = True
    elif "y" in re: br=False
    else:
        print("Инвалидные данные, использую данные по-умолчанию (N)")
        print("Всё прошло успешно!")
        br = True
    if br: break
input()