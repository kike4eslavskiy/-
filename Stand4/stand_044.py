import timeit
from dexter import dexter

def test():
    graph = {} #Создает пустой словарь graph
    
    start_time = timeit.default_timer() #Записывает текущее время в переменной start_time
    result = dexter(graph, 'A') #Вызывает функцию dexter, передавая ей пустой граф graph и вершину A
    elapsed_time = timeit.default_timer() - start_time #Измеряет время, прошедшее с момента запуска функции
    
    print("Кратчайшие расстояния:")
    for vertex, distance in result.items(): #Начинает цикл по элементам словаря result
        print(f"{vertex}: {distance}")
    
    print(f"\nВремя выполнения: {elapsed_time:.6f} секунд")

if name == "__main__": #Проверяет, выполняется ли данный модуль как основная программа.
    test()