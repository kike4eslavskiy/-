import timeit
def fun(): # Создаём упорядоченный массив случайных чисел
    arr = sorted(random.sample(range(100, 800), 50))  # 50 уникальных чисел от 100 до 800
    target = random.randint(100, 800)  # Случайное значение для поиска
    
    # Производим бинарный поиск
    index, operations = binary_search(arr, target)
    
    return index, operations


    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')