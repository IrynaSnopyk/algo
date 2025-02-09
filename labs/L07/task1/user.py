
"""
Реалізуйте алгоритм сортування обміном (бульбашкове сортування).
"""

N = 10000    # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


# Sorting time:  40.453125
# Errors:        0

def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for pasNum in range(n - 1, 0, -1):
        for i in range(pasNum):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


