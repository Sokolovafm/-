name = str(input("Введите имя: "))
surname = str(input("Введите фамилию: "))
age = int(input("Сколько вам полных лет?: "))
weight = int(input("Ваш вес в килограммах?: "))

result = f"{name} {surname}, {age} год, вес {weight}"

def bad_condition():
    if age < 30:
        print(result + " - сейчас заняться собой будет куда проще, чем в тридцать!")
    elif 30 < age < 40:
        print(result + " - следует заняться собой")
    else:
        print(result + " - следует обратиться к врачу!")

if 50 < weight < 120:
    print(result + " - хорошее состояние")
else: bad_condition()
