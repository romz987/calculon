import logging
from collections import namedtuple
from colorama import init, Fore, Style


# Уровень логирования
logging.basicConfig(level=logging.INFO)
# Инициализируем coloram-у
init(autoreset=True)




def wbprice_request(stuff, tab):
    """
    Считаем цену для Wildberries
    """
    # Тест
    logging.info (
        f'{Fore.BLUE}[wbcalc.py][wbprice_request] ' 
        f'output:{Style.RESET_ALL}\nstuff is: {stuff}'
    )

    # Список для результатов
    results = []
    # Начинаем расчеты для каждого комплекта
    for count, (
        wage, 
        cost_box, 
        package, 
        des_percent, 
        cperc,  
        tax_percent, 
        risk,
        cost_per_one,
        shipment,
        fbso
    ) in stuff.items():

        # Себестоимость
        cost_row = int(count) * float(cost_per_one)
        des_profit = cost_row * (float(des_percent) / 100)
        # Логистика
        package = _pack_size(package)  
        logistics = _logistics_wb(package)

        # Запаковываем
        calcdata = calcdata_strct(
            count = count,
            cost_row = cost_row,
            des_profit = des_profit,
            logistics = logistics,
            cperc = cperc,
            risk = risk,
            tax_percent = tax_percent,
            cost_box = cost_box,
            wage = wage
        )

        # Отправляем на расчет
        price = _wb_calculate(tab, calcdata)
        # Возвращаем структуру цены
        result = _price_struct(tab, calcdata, price)
        # Пихаем в список
        results.append(result)

    return results


def wbprofit_request(stuff):

    answer="WBSPROFIT_request"

    return answer


def _wb_calculate(tab, calcdata):
    """ 
    Логика нахождения цены
    """
    # Условия
    tolerance = 0.1
    max_iterations = 1000

    # Ожидаемый профит
    des_profit = float(calcdata.des_profit)

    # Начальное приближение
    price = (
        (calcdata.cost_row + calcdata.logistics + calcdata.des_profit
        + float(calcdata.wage) + float(calcdata.cost_box))
        * (1 + (float(calcdata.cperc) / 100))
    )

    print(f'price is: {price}')

    # Расчет
    for i in range(1, max_iterations):

        if tab == 'WBsole':
            price = _price_calc_sole(calcdata, price)
            profit = _profit_calc_sole(calcdata, price)

        elif tab == 'WBltd':
            price = _price_calc_ltd(calcdata, price)
            profit = _profit_calc_ltd(calcdata, price)

        else:
            print('TabError')
            break

        # Сраниваем
        diff = abs(profit - des_profit)

        # Возвращаем решение, только если оно найдено
        if diff <= tolerance:
            return round(price) 
    
    logging.info(f'{Fore.RED}Не удалось найти решение{Style.RESET_ALL}')
    return 0


def _price_calc_sole(calcdata, price):
    """ 
    Считает цену для WB ИП

    :param calcdata: именованный кортеж со значениями полей
    :param price: начальное приближение цены

    :return: price
    """
    # Комиссии, налоги, риски
    comissions = price * (float(calcdata.cperc) / 100)
    tax = price * (float(calcdata.tax_percent) / 100)
    risk = price * (float(calcdata.risk) / 100)
    # Все расходы
    all_costs = (
            calcdata.cost_row + comissions + calcdata.logistics
            + float(calcdata.cost_box) + float(calcdata.wage) + risk + tax
        )
    # Цена
    price = all_costs + calcdata.des_profit

    return price


def _profit_calc_sole(calcdata, price):
    """ 
    Считает профит для WB ИП

    :param calcdata:  именованный кортеж со значениями полей
    :param price: рассчитанная в _price_calc_sole цена
    """
    # Комиссии, налоги, риски
    comissions = price * (float(calcdata.cperc) / 100)
    tax = price * (float(calcdata.tax_percent) / 100)
    risk = price * (float(calcdata.risk) / 100)
    # Все расходы
    all_costs = (
            calcdata.cost_row + comissions + calcdata.logistics
            + float(calcdata.cost_box) + float(calcdata.wage) + risk + tax
        )
    # Профит
    profit = price - all_costs

    return profit


def _price_calc_ltd(calcdata, price):
    """ 
    Считает цену для WB ООО

    :param calcdata: именованный кортеж со значениями полей
    :param price: начальное приближение цены

    :return: price
    """
    print(f'we in _price_calc_ltd method')

    # Комиссии, налоги, риски
    comissions = price * (float(calcdata.cperc) / 100)
    risk = price * (float(calcdata.risk) / 100)
    # Все расходы без рисков и налогов
    all_costs = (
                calcdata.cost_row + comissions + calcdata.logistics 
                + float(calcdata.cost_box) + float(calcdata.wage)
        )
    # Считаем налог
    tax = (price - all_costs) * (float(calcdata.tax_percent) / 100) 
    # Цена
    price = all_costs + tax + risk + calcdata.des_profit

    return price


def _profit_calc_ltd(calcdata, price):
    """ 
    Считает профит для WB ООО

    :param calcdata: именованный кортеж со значениями полей
    :param price: начальное приближение цены

    :return: price
    """
    print(f'we in _profit_calc_ltd method')

    # Комиссии, налоги, риски
    comissions = price * (float(calcdata.cperc) / 100)
    risk = price * (float(calcdata.risk) / 100)
    # Все расходы без рисков и налогов
    all_costs = (
            calcdata.cost_row + comissions + calcdata.logistics 
            + float(calcdata.cost_box) + float(calcdata.wage)
        )
    # Считаем налог
    tax = (price - all_costs) * (float(calcdata.tax_percent) / 100) 
    # Цена
    profit = price - (all_costs + tax + risk)

    return profit


def _price_struct(tab, calcdata, price):
    """  
    Возвращаем структуру цены
    """
    print(tab)
    if tab == 'WBsole':
        comissions = round(price * (float(calcdata.cperc) / 100))
        risk = round(price * (float(calcdata.risk) / 100))
        tax = round(price * (float(calcdata.tax_percent) / 100))
        all_costs = (
                round(calcdata.cost_row + comissions + calcdata.logistics 
                + float(calcdata.cost_box) + float(calcdata.wage) + risk + tax)
            )
        profit = round(price - all_costs)

    elif tab == 'WBltd':
        comissions = round(price * (float(calcdata.cperc) / 100))
        risk = round(price * (float(calcdata.risk) / 100))
        all_costs = (
                round(calcdata.cost_row + comissions + calcdata.logistics 
                + float(calcdata.cost_box) + float(calcdata.wage))
            )
        tax = round((price - all_costs) * (float(calcdata.tax_percent) / 100))
        profit = round(price - (all_costs + tax + risk))

    else:
        logging.info(
            f'{Fore.RED}[wbcalc][_price_struct]TabError{Style.RESET_ALL}'
        )

    answr_data = answerdata_strct(
        count = calcdata.count,
        price = price,
        profit = profit,
        cost_row = calcdata.cost_row,
        comissions = comissions,
        logistics = calcdata.logistics,
        tax = tax,
        risk = risk,
    )

    return answr_data


def _pack_size(package):
    """
    Считаем объем упаковки из строки

    :param package: строка с размером упаковки

    :return: объем в милилитрах
    """

    # Преобразуем каждую часть строки в целое число
    numbers = map(int, package.split('*'))          
    result = 1
    for number in numbers:
        result *= number
   
    result = result / 1000


    return result


def _logistics_wb(package):
    """
    Считаем цену логистики в зависимости
    от объема упаковки

    :param package: объем в литрах

    :return: цена
    """
    if package < 5:
        factor = 5
    else:
        factor = 6

    result = 30 + factor + factor * ((package - 0.01) // 1)

    return result


# Cтруктура данных для запроса на расчет
calcdata_strct = namedtuple('calcdata_strct', [
    'count',
    'cost_row',
    'des_profit',
    'logistics',
    'cperc',
    'risk',
    'tax_percent',
    'cost_box',
    'wage'
])


# Структура данных для ответа
answerdata_strct = namedtuple('answerdata_strct', [
    'count',
    'price',
    'profit',  
    'cost_row',
    'comissions',
    'logistics',
    'tax',
    'risk'
])



# Тест 
stuff = {'1': ['8', '8', '25*20*17', '50', '21', '7', '5', '150', [], []]}
tab = 'WBltd'



var = wbprice_request(stuff, tab)

print(var)
print('buy')
