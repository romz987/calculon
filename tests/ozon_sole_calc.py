def ozs_calculate(cost_row, des_percent, cperc, cfix, logistics, cost_box, wage, tax_percent, risk):
    """ 
    Основная логика для OZON ИП

    :param cost_row: Себестоимость товара 
    :param des_percent: Ожидаемый процент прибыли от себеса
    :param cperc: Вознаграждение Ozon (18%) + Эквайринг (1.5%)
    :param cfix: Обработка отправления (30rub)
    :param logistics: Логистика за литры  
    :param cost_box: Стоимость упаковки
    :param wage: Стоимсоть труда
    :tax_percent: Процент налога
    :risk: Процент рисков

    """
    tolerance = 0.1
    max_iterations = 1000

    # Ожидаемый профит от себеса
    des_profit = cost_row * (des_percent / 100)
    
    # Начальное приближение
    # price = (cost_row + des_profit + cost_box + wage + cfix + logistics) * (1 + cprec / 100)
    price = (cost_row + des_profit + cfix + logistics + cost_box + wage)

    # Расчеты 
    for i in range(1, max_iterations):
        # Считаем цену
        price = price_calc_sole(
            cost_row,
            des_profit,
            price,
            logistics,
            cperc,
            risk,
            tax_percent,
            cfix,
            cost_box,
            wage
        )

        # Проверяем на соответствие ожидаемой прибыли
        profit = profit_calc_sole(
            cost_row,
            des_profit,
            price,
            logistics,
            cperc,
            risk,
            tax_percent,
            cfix,
            cost_box,
            wage
        )

        # Сраниваем
        diff = abs(profit - des_profit)

        if diff <= tolerance:
            break 

        if i >= max_iterations:
            print('Не удалось найти решение')
            price = None 
            break


    return price


def price_calc_sole(cost_row, des_profit, price, logistics, cperc, risk, tax_percent, cfix, cost_box, wage):
    """
    Считаем цену для ИП 
    :cost_row: Себестоимость
    :des_profit: Профит в рублях(от себеса)
    :param price: Начальное приближение
    :param logistics: Логистика
    :param cperc: Проценты Оzon (Вознаграждение + Эквайринг)
    :param risk: Процент рисков
    :param tax_percent: Процент налога
    :param cfix: Обработка отправления (30rub)
    :param cost_box: Стоимсоть упаковки
    :param wage: Стоимость труда

    """
    # Последняя миля
    print(f'последняя миля: {lastmile(price)}')
    # Все комисии 
    comissions = price * (cperc / 100) + cfix + lastmile(price) + logistics
    # Налог
    tax = price * (tax_percent / 100)
    # Риски
    risks = price * (risk / 100) 
    # Все расходы
    all_costs = cost_row + comissions + tax + risks + cost_box + wage 
    # Цена
    price = all_costs + des_profit 


    return price


def profit_calc_sole(cost_row, des_profit, price, logistics, cperc, risk, tax_percent, cfix, cost_box, wage):
    """
    Считаем цену для ИП 
    :cost_row: Себестоимость
    :des_profit: Профит в рублях(от себеса)
    :param price: Начальное приближение
    :param logistics: Логистика
    :param cperc: Проценты Оzon (Вознаграждение + Эквайринг)
    :param risk: Процент рисков
    :param tax_percent: Процент налога
    :param cfix: Обработка отправления (30rub)
    :param cost_box: Стоимсоть упаковки
    :param wage: Стоимость труда

    """
    # Все комисии 
    comissions = price * (cperc / 100) + cfix + lastmile(price) + logistics
    # Налог
    tax = price * (tax_percent / 100)
    # Риски
    risks = price * (risk / 100) 
    # Все расходшы
    all_costs = cost_row + comissions + tax + risks + cost_box + wage
    # Профит
    profit = price - all_costs


    return profit



def lastmile(price):
    """ 
    Считем последнюю милю
    5.5% от цены, но не больше 500 руб

    :param price: 
    """
    result = price * 0.055

    if result < 500:
        pass
    elif result > 500:
        result = 500 
    else:
        print('lastmile value error')

    return result



# # Тест
# cost_row = 38.08
# des_percent = 20
# cperc = 18.5
# cfix = 0
# logistics = 32
# cost_box = 3
# wage = 3
# tax_percent = 7
# risk = 3
#
#
# list = [1, 2, 3, 4]
# i
# for i in list:
#     row = cost_row * i 
#     
#     # Считаем 
#     result = ozs_calculate(
#         row,
#         des_percent,
#         cperc,
#         cfix,
#         logistics,
#         cost_box,
#         wage,
#         tax_percent,
#         risk
#     )
#
#     result = round(result)
#     
#     # Выводим 
#     print(f'Цена за {i} ед: {result} руб')
#
# # Прощаемся
# print('buy')



relust = profit_calc_sole(
    cost_row = 38.08, 
    des_profit = 20, 
    price = 165, 
    logistics = 32, 
    cperc = 18.5, 
    risk = 0, 
    tax_percent = 7, 
    cfix = 0, 
    cost_box = 3, 
    wage = 3)

print(relust)





