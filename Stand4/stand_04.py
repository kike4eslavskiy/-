def dexter(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set() #Создание пустого множества visited, которое будет содержать вершины, которые уже были посещены
    
    while len(visited) < len(graph): #Начало цикла, который продолжается до тех пор, пока не будут посещены все вершины в графе
        current_vertex = None
        min_distance = float('infinity') #Инициализируем current_vertex как None, что будет использоваться для хранения текущей вершины. Инициализация min_distance как бесконечности, чтобы мы могли потом сравнить расстояния
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance: #Проверка, не была ли текущая вершина vertex ранее посещена и меньше ли её расстояние, чем min_distance.
                min_distance = distances[vertex]
                current_vertex = vertex
        
        if current_vertex is None:
            break #Если current_vertex все еще None, это означает, что в графе нет достижимых вершин, и выполнение цикла может быть завершено
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances