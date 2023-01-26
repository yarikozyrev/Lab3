ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'*1000000
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10000000
message=input('введите текст ЗАГЛАВНЫМИ буквами русского или английского алфавита: ')
lang=input('введите язык RU или EU: ')
number=int(input('введите шаг сдвига (не более 1000000) ')) #создаем переменную с шагом шифрования
b = '' #создаем переменную для вывода
if lang == 'RU':
    for i in message:
        place=ru.find(i) #вычисляем места символов в списке
        new=place+number #сдвигаем символы на шаг, указанный в переменной smeshenie
        if i in ru:
            b+=ru[new] #задаем значения
        else:
            b+=i
else: #то же самое с другим языком
    for i in message:
        place=eu.find(i)
        new=place+number
        if i in eu:
            b+=eu[new]
        else:
            b+=i
print(b)
