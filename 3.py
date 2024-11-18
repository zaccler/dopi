def beauty_degree(n, arr):
    # Множество уникальных чисел для проверки
    unique_numbers = set(arr)
    
    # Проверяем наличие всех чисел 1, 2, ..., max(arr)
    for i in range(1, max(arr) + 1):
        if i not in unique_numbers:
            return 0
    
    # Подсчёт отрезков
    current_min = 1
    segments = 0
    for num in arr:
        if num == current_min:  # Текущий минимум найден
            current_min += 1
            segments += 1
    
    return segments

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вычисление степени красоты
result = beauty_degree(n, arr)
print(result)
