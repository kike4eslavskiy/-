import heapq

def dijkstra(graph, start):
     # Инициализация: расстояние до всех вершин - бесконечность, кроме стартовой
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
     # Очередь с приоритетом (куча), храним (расстояние, вершину)
    priority_queue = [(0, start)]  # Приоритетная очередь (куча)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше известного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Если нашли более короткий путь до соседа, обновляем
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример графа (в виде словаря словарей)
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