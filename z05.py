import heapq

def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # Приоритетная очередь (куча)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше известного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример использования
print(dijkstra(graph, 0))  # Вывод: {0: 0, 1: 1, 2: 3, 3: 4}