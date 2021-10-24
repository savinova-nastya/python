"""
Инвест. проект заключается в том, что будем производить карликовые бананы и поставлять в разные близлежащие страны
Первоначальные затраты: 800 тысяч долл. на закупку семян и необходимого оборудования(земля своя есть).
Регулярный доход: 600 тыс долл. от продажи карликовых бананов
Регулярный расход: 200 тыс долл. на зарплату персоналу, кормежку кроликов и т д
Срок реализации проекта: 20 лет на содержание, полив, подкормку, зарплату сотрудникам, налоги и т д
Ставка дисконтирования: 20%
"""
from itertools import accumulate
from functools import partial
import math


def calcNPV(cost0, income, cost, n, r):
    """Функция вычисляет NPV и DPP проекта"""

    NPVlist = [-cost0] + [(income - cost) / (1 + r) ** i for i in range(1, n + 1)]
    NPVaccum = list(accumulate(NPVlist))
    NPV = NPVaccum[-1]
    m = len([npvacc for npvacc in NPVaccum if npvacc < 0]) - 1
    DPP = m + abs(NPVaccum[m]) / NPVlist[m + 1] if len(NPVlist) > m + 1 else None
    return NPV, DPP


cost0 = 800
income = 600
cost = 200
n = 20
r = 0.2

NPV, DPP = calcNPV(cost0, income, cost, n, r)

calcNPV0 = partial(calcNPV, cost0=cost0, income=income, cost=cost, n=n)
minNPV, IRR = math.inf, None
for r in range(1, 101):
    NPVirr = calcNPV0(r=r / 100)[0]
    if abs(NPVirr) < abs(minNPV):
        minNPV, IRR = NPVirr, r / 100

if IRR <= 0.02 or IRR >= 0.99:
    print("Скорее всего, IRR проекта с текущими параметрами отсутствует"
          " либо выбран слишком узкий диапазон изменения ставки ")
    IRR = None
print(f"NPV = {NPV}, DPP = {DPP}, IRR = {IRR}:\tПроект {'' if NPV > 0 else 'Не'}Эффективен!")


