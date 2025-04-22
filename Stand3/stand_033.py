import timeit
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
      time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')