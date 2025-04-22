import timeit
for i in array:
    if i < min_1:
        min_2 = min_1
        min_1 = i 
    elif min_1 == min_2 != i:  # равны ли min1 и min2 и отличается ли текущее значение i
        min_2 = i
    else:
        if min_1 > i < min_2:  # Если i меньше, то i становится новым мин вторым значением
            min_2 = i
time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')
        