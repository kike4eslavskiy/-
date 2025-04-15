array = [2, 1, 1, 2, 3, 5]
min_1 = array[0]  #Переменной присваивается первое значение из массива
min_2 = array[1]
for i in array:
    if i < min_1:
        min_2 = min_1
        min_1 = i 
    elif min_1 == min_2 != i: #равны ли min1 и min2 и отличается ли текущее значение i
        min_2 = i
    else:
        if min_1 > i < min_2: #Если i меньше, то i становится новым мин вторым значением
            min_2 = i
if min_1 == min_2:
    print(f'Массив состоит из одинаковых элементов')
print(min_1, min_2)