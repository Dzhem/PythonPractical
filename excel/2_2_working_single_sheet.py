import xlrd
import random


#   функция нахождения медианы
#   возможно, стоило использавать функцию  from statistics import median
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        # assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


rd = xlrd.open_workbook('salaries.xlsx')
sheet = rd.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#   полчаем список медиан зарплаты
rownum = 1
salaries_median = []
while rownum < len(vals):
    salaries_median.append(quickselect_median(vals[rownum][1:]))
    rownum += 1

#   выводим название региона с самым большим значением медианы
ind_max_median = 0
i = 0
prev_salary = salaries_median[0]
for salary in salaries_median:
    if salary > prev_salary:
        ind_max_median = i
    prev_salary = salary
    i += 1

# получаем среднюю зарплату по должности
average_salaries = []
tmp_list = [tmp for tmp in vals[1:]]
i = 0
j = 1
while j < 8:
    sum = 0
    while i < len(tmp_list):
        sum += (tmp_list[i][j])
        i += 1
    average_salaries.append(sum / i)
    i = 0
    j += 1

#   выводим результат
print(vals[ind_max_median + 1][0],
      vals[0][average_salaries.index(max(average_salaries)) + 1])
