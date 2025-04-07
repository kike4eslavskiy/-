import timeit
import random

def binary_search(arr, target): # Функция бинарного поиска: arr - массив, target - значение, которое надо найти
    left, right = 0, len(arr) - 1 
    operations = 0

    while left <= right:
        operations += 1  # Считаем каждую операцию сравнения
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid, operations  # Возвращаем индекс найденного элемента и количество операций
    
    return -1, operations  # Возвращаем -1, если элемент не найден

def fun():
    # Создаём упорядоченный массив случайных чисел
    arr = sorted(random.sample(range(100, 800), 50))  # 50 уникальных чисел от 100 до 800
    target = random.randint(100, 800)  # Случайное значение для поиска
    
    # Производим бинарный поиск
    index, operations = binary_search(arr, target)
    
    return index, operations

start = timeit.default_timer()
print("The start time is:", start)

index, operations = fun()
print("Index of the target is:", index)
print("Number of operations:", operations)
print("The difference of time is:", timeit.default_timer() - start)