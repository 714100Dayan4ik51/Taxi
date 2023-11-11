import itertools


def find_optimal_route(distances, tariffs):
    n = len(distances)  # количество сотрудников
    m = len(tariffs)  # количество такси

    # все возможные перестановки сотрудников
    permutations = list(itertools.permutations(range(n)))

    min_cost = float('inf')  # минимальная стоимость
    optimal_route = None

    for route in permutations:
        cost = 0

        # Вычисляем стоимость для текущего маршрута
        for i in range(n):
            driver = route[i] % m
            distance = distances[i]
            tariff = tariffs[driver]
            cost += distance * tariff

        if cost < min_cost:
            min_cost = cost
            optimal_route = route

    return optimal_route, min_cost

n = int(input("Введите кол-во сотрудников >> "))
distances = list(map(int,input("Введите расстояние в км до дома (через пробел) >> ").split()))
tariffs = list(map(int,input("Введите цену на такси (через пробел) >> ").split()))
optimal_route, min_cost = find_optimal_route(distances, tariffs)
