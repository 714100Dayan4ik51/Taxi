import itertools
from num2words import num2words

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
if n < 1:
    print("Число не может быть меньше одного!")
    exit()
distances = list(map(int,input("Введите расстояние в км до дома (через пробел) >> ").split()))
tariffs = list(map(int,input("Введите цену на такси (через пробел) >> ").split()))
optimal_route, min_cost = find_optimal_route(distances, tariffs)
def number_to_words(num):
    words = num2words(num, lang='ru')
    ending = num % 10
    if ending == 1 and num % 100 != 11:
        end = " рубль"
    elif 1 < ending < 5 and (num % 100 < 10 or num % 100 > 21):
        end = " рубля"
    else:
        end = " рублей"
    result = words.capitalize() + end
    return result
print("Оптимальный маршрут: ", optimal_route)
print("Минимальная стоимость: ", number_to_words(min_cost))