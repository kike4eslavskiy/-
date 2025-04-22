import time
Grapf = [[0,1], [0,2], [0,3], [2,3], [1,6], [4,5]]
start_time = time.time()
def update_matrix(matrixOfConnections, graph, level, current_node):
    nodes = count_nodes(graph)[0] #Получает список всех узлов в графе
    for i in nodes:
        if edge_exsist(current_node, i, graph): #Проверяется, существует ли связь между current_node и i
            if current_node == i:
                continue
            matrixOfConnections[current_node][i] = level + 1 # Если связь существует, то уровень до узла i обновляется

def search_connection(a, b, graph):
    start = a
    end = b
    matrixOfConnections = initialize_matrix(count_nodes(graph)[1])
    level = 1
    current_node = 0
    nodes = count_nodes(graph)[0] #Получаем список всех узлов в графе
    for node in nodes: #Цикл проходит по всем узлам в графе и сбрасывает уровень на 1 для каждого нового узла
        level = 1
        for i in nodes:
            if edge_exsist(current_node, i, graph): #Сущ ли связь от current_node до i 
                if current_node == i:
                    continue
                matrixOfConnections[current_node][i] = level + 1 #Если связь между current_node и i существует, уровень устанавливается, как level + 1
        level += 1
        current_node += 1

    return matrixOfConnections

def count_nodes(graph):
    amount_of_nodes = list(set([i for l in graph for i in l])) #Создается список уникальных узлов, включая все узлы из всех рёбер
    return amount_of_nodes, len(amount_of_nodes) #Возвращаем список узлов и их количество

def edge_exsist(current_node, next_node, graph): #Существует ли ребро между current_node и next_node.
    for i in graph:
        if (current_node in i) and (next_node in i): #Проверяем, находится ли current_node и next_node в одном и том же ребре.
            return True
        else:
            continue
    return False

def initialize_matrix(amount_of_nodes): #Определяем функцию для инициализации матрицы соединений.
    matrix = []
    for i in range(amount_of_nodes):
        array = [0 for _ in range(amount_of_nodes)] #Создаём строку из нулей для текущего узла
        array[i] = 1
        matrix.append(array) #Добавляет строку в матрицу
    return matrix #Возвращаем матрицу соединений

for i in search_connection(1, 2, Grapf):
    print(i)
    end_time = time.time() # Записываем время окончания выполнения программы
execution_time = end_time - start_time # Вычисляем и выводим время выполнения
print(f'Время выполнения программы: {execution_time:.6f} секунд')