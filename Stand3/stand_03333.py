import timeit
def edge_exsist(current_node, next_node, graph): #Существует ли ребро между current_node и next_node.
    for i in graph:
        if (current_node in i) and (next_node in i): #Проверяем, находится ли current_node и next_node в одном и том же ребре.
            return True
        else:
            continue
    return False
   time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')