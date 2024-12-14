#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# С помощью алгоритма поиска в глубину находим минимальное расстояние между начальным и конечным пунктами
import itertools


def dfs(start, end, visited, current_distance, min_distance, distance_matrix):
    """Поиск в глубину для нахождения минимального расстояния."""
    if start == end:
        return min(current_distance, min_distance)

    for next_city in range(len(distance_matrix)):
        if not visited[next_city]:
            visited[next_city] = True
            current_distance += distance_matrix[start][next_city]
            min_distance = dfs(next_city, end, visited, current_distance, min_distance, distance_matrix)
            current_distance -= distance_matrix[start][next_city]
            visited[next_city] = False  # Backtrack

    return min_distance


def find_min_distance_dfs(distance_matrix, start, end):
    """Ищем минимальное расстояние между начальным и конечным пунктами."""
    visited = [False] * len(distance_matrix)
    visited[start] = True
    return dfs(start, end, visited, 0, float('inf'), distance_matrix)


# Пример использования
if __name__ == "__main__":
    # Новая матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 83, 224, 433, 549, 729, 886, 552, 441, 192],
        [83, 0, 150, 359, 475, 655, 812, 478, 367, 275],
        [224, 150, 0, 209, 325, 505, 662, 328, 217, 416],
        [433, 359, 209, 0, 116, 296, 453, 537, 426, 625],
        [549, 475, 325, 116, 0, 180, 337, 431, 542, 741],
        [729, 655, 505, 296, 180, 0, 157, 251, 362, 633],
        [886, 812, 662, 453, 337, 157, 0, 342, 453, 724],
        [552, 478, 328, 537, 431, 251, 342, 0, 111, 382],
        [441, 367, 217, 426, 542, 362, 453, 111, 0, 493],
        [192, 275, 416, 625, 741, 633, 724, 382, 493, 0],
    ]

    start_city = 0  # Начальный пункт
    end_city = 9  # Конечный пункт

    # Поиск с помощью DFS
    min_distance_dfs = find_min_distance_dfs(distance_matrix, start_city, end_city)

    # Решение задачи коммивояжера
    def calculate_total_distance(route, distance_matrix):
        """Вычисление общей дистанции для данного маршрута."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += distance_matrix[route[i]][route[i + 1]]
        return total_distance

    print(f"Минимальное расстояние с помощью DFS от пункта {start_city} до {end_city}: {min_distance_dfs}")
