import timeit
def update_matrix(matrixOfConnections, graph, level, current_node):
    nodes = count_nodes(graph)[0] #Получает список всех узлов в графе
    for i in nodes:
        if edge_exsist(current_node, i, graph): #Проверяется, существует ли связь между current_node и i
            if current_node == i:
                continue
            matrixOfConnections[current_node][i] = level + 1 # Если связь существует, то уровень до узла i обновляется

            
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')