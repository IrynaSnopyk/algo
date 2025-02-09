
"""
Реалізуйте алгоритм сортування вставкою
"""

N = 10000    # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000

# Sorting time:  25.140625
# Errors:        0

def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for index in range(1, n):
        current = array[index]
        for i in range(index - 1, -1, -1):
            if array[i] > current:
                array[i + 1] = array[i]
            else:
                array[i + 1] = current
                break
