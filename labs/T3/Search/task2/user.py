"""
Реалізуйте алгоритм пошуку номеру найпершого входження до заданого масиву, заданого числа x.
Якщо заданий елемент відсутній у списку - поверніть номер першого елементу, що більший за число x:
                            array[i] >= x
"""


def bsearch_leftmost(array, x):
    """ Бінарний пошук для відшукання найпершого входження заданого числа

    :param array: Відсортований за неспаданням масив цілих чисел
    :param x:     Шукане число
    :return:      Номер шуканого елемента у масиві
    """
    left = 0  # Індекс лівого елементу
    right = len(array)  # Індекс правого елементу
    while left < right:
        m = left + (right - left) // 2  # Середина відрізка
        if array[m] < x:
            left = m + 1
        else:
            right = m

    return left
