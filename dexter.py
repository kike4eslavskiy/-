import heapq

def dijkstra(graph, start):
     # Инициализация: расстояние до всех вершин - бесконечность, кроме стартовой
    distances = {vertex: float('inf') for vertex in graph} #Cоздает словарь distances, в котором инициализируются расстояния до всех вершин графа
    distances[start] = 0 
     # Очередь с приоритетом (куча), храним (расстояние, вершину)
    priority_queue = [(0, start)]  # Приоритетная очередь (куча)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue) #Извлекаем вершину с наименьшим расстоянием из приоритетной очереди

        # Если текущее расстояние больше известного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex].items(): #Cосед(neighbor) и вес ребра(weight), который соединяет current_vertex и neighbor
            distance = current_distance + weight
            # Если нашли более короткий путь до соседа, обновляем
            if distance < distances[neighbor]: #Мы складываем текущее расстояние и вес ребра, чтобы получить полное расстояние от начальной вершины до соседа
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) #Добавляем соседа в приоритетную очередь с его обновленным расстоянием, чтобы позже его также обработать

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(f"Кратчайшие расстояния от вершины {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"До {vertex}: {distance}")

    def dexter(graph, start):
    distances = {vertex: float('infinity') for vertex in graph} #Создание словаря distances, который будет хранить кратчайшие расстояния от начальной вершины до каждой вершины графа
    distances[start] = 0
    visited = set() #Создание пустого множества visited, которое будет содержать вершины, которые уже были посещены
    
    while len(visited) < len(graph): #Начало цикла, который продолжается до тех пор, пока не будут посещены все вершины в графе
        current_vertex = None
        min_distance = float('infinity') #Инициализируем current_vertex как None, что будет использоваться для хранения текущей вершины. Инициализация min_distance как бесконечности, для сравнения расстояния
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex
        
        if current_vertex is None:
            break
        
        visited.add(current_vertex) #Добавление текущей вершины current_vertex в множество посещенных вершин
        
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances