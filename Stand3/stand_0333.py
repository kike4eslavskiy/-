import timeit
def count_nodes(graph):
    amount_of_nodes = list(set([i for l in graph for i in l])) #Создается список уникальных узлов, включая все узлы из всех рёбер
    return amount_of_nodes, len(amount_of_nodes) #Возвращаем список узлов и их количество
    time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')