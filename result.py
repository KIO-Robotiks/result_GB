def get_small_array(array):
    for i in array:
        if len(i) > 3:
            array.remove(i)


print("Программа принимает массив из строк и воводит массив из тех строк, у которых длинна <= 3 символа")
print("Зададим массив..")
array = []
count = 1
while 1:
    i = input(f'Введите элемент № {count}. Для окончания ввода нажмите "q": ')
    if i == 'q':
        break
    else:
        array.append(i)
    count +=1

get_small_array(array)
print(array)
