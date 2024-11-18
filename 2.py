def min_distance(n, m, costs):
    # Отсортировать пробирки по стоимости (сохраняя индексы)
    indexed_costs = sorted((cost, index) for index, cost in enumerate(costs))
    
    # Выбрать m пробирок с минимальной стоимостью
    selected = sorted(index for _, index in indexed_costs[:m])
    
    # Вычислить минимальное расстояние
    return selected[-1] - selected[0] + 1

# Чтение входных данных
n, m = map(int, input().split())
costs = list(map(int, input().split()))

# Вычисление и вывод результата
result = min_distance(n, m, costs)
print(result)
