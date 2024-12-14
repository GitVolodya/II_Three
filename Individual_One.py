#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Поиск самого длинного пути в матрице

def longest_path(matrix, start_char):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    memo = {}

    def dfs(x, y, prev_char):
        if (x, y) in memo:
            return memo[(x, y)]

        max_length = 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < rows and 0 <= new_y < cols and
                    ord(matrix[new_x][new_y]) == ord(prev_char) + 1):
                max_length = max(max_length, 1 + dfs(new_x, new_y, matrix[new_x][new_y]))

        memo[(x, y)] = max_length
        return max_length

    longest = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == start_char:
                longest = max(longest, dfs(i, j, start_char))

    return longest

# Новая матрица
new_matrix = [
    ["E", "F", "G", "H"],
    ["D", "C", "B", "I"],
    ["A", "J", "K", "L"],
    ["M", "N", "O", "P"],
]
start_char = 'E'  # Начальный символ

# Подсчет самого длинного пути
longest_path_length = longest_path(new_matrix, start_char)

print(longest_path_length)  # Вывод: длина самого длинного пути
