earning = int(input('Выручка: '))
costs = int(input('Издержки: '))

if costs > earning:
    print('Убыток:')
elif earning > costs:
    print('Прибыль:')
    profitability = (earning - costs) / earning
    print(f'Рентабельность: {profitability}')
    empl_count = int(input('Количество штатных сотрудников: '))
    profit_per_empl = (earning - costs) / empl_count
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_per_empl}')
elif earning == costs:
     print ('Финансовый результат = 0')