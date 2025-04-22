import timeit
def initialize_matrix(amount_of_nodes): #Определяем функцию для инициализации матрицы соединений.
    matrix = []
    for i in range(amount_of_nodes):
        array = [0 for _ in range(amount_of_nodes)] #Создаём строку из нулей для текущего узла
        array[i] = 1
        matrix.append(array) #Добавляет строку в матрицу
    return matrix #Возвращаем матрицу соединений
 time = timeit.default_timer() - start
    return ("%.10f" % time).rstrip('0')