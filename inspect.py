def inspect(func):
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        print(f'Retvalue: {rv}')
    return wrapper

@inspect
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
    return(text)

strings = []
cnt = 1
print("Ввод значений: ")
while str:
    str = input(f'Введите {cnt}-е строковое значение: ')
    if str != '':
        strings.append(str)
        cnt += 1
    else:
        break
r = bool(input('Если хотите выполнить "склеивание" с конца списка - введите True (по умолчанию значение False): '))

concat(strings, reversed = r)