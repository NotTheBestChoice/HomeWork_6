def concat(*strings, reversed: bool):
    lst = strings[0]
    text = ''
    if reversed == True:
        lst.reverse()
        for i in lst:
            text += i + ' '
    else:
        for i in lst:
            text += i + ' '
    print(text)
    return(text)

strings = []
cnt = 1
print("Проверка функции конкатенации строковых значений.")
print("Вводите значения последовательно в любом количестве.")
print("Для завершения ввода подстрок нажмите Enter.")
while str:
    str = input(f'Введите {cnt}-е строковое значение: ')
    if str != '':
        strings.append(str)
        cnt += 1
    else:
        break
r = bool(input('Если хотите выполнить "склеивание" с конца списка - введите True (по умолчанию значение False): '))

concat(strings, reversed = r)