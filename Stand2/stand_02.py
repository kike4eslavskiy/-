import timeit
def binary_search(arr, target): # Функция бинарного поиска: arr - массив, target - значение, которое надо найти
    left, right = 0, len(arr) - 1 #left первый элемент массива, а right последний элемент
    operations = 0

    while left <= right:
        operations += 1  # Считаем каждую операцию сравнения
        mid = (left + right) // 2 # Индекс середины текущего диапазона поиска
        
        if arr[mid] < target: # Меньше ли индекс середины значения target.
            left = mid + 1 
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid, operations  # Возвращаем индекс найденного элемента и количество операций
    
    return -1, operations  # Возвращаем -1, если элемент не найден

    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')