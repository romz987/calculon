import logging 
import math
from collections import namedtuple
from colorama import init, Fore, Style


# Уровень логирования
logging.basicConfig(level=logging.INFO)
# Инициализируем coloram-у
init(autoreset=True)


class OZCalc():


    # Cтруктура данных для запроса на расчет
    calcdata_oz = namedtuple('calcdata', [
        'cost_row',
        'des_profit',
        'logistics',
        'cperc',
        'risk',
        'tax_percent',
        'cost_box',
        'wage',
        'shipment'
    ])

    # Структура данных для ответа
    answerdata_oz = namedtuple('answerdata', [
        'price',
        'profit',
        'des_profit',
        'cost_row',
        'comissions',
        'logistics',
        'tax',
        'risk'
    ])


    
    def ozprice_request(self, stuff, tab):
        """
        Считаем цену для OZON
        """
        # Лог
        logging.info(
            f'{Fore.GREEN}[ozcalc.py][ozprice_request]'
            f'output:{Style.RESET_ALL}\nstuff is: {stuff}'
            f'\ntab is: {tab}'
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
            package = self._pack_size(package)

            print(fbso)
            # FBS vs FBO 
            if fbso[0] == "fbs":
                logistics = self._logistics_oz_fbs(package)
                shipment = shipment[0]
            elif fbso[0] == "fbo":
                logistics = self._logistics_oz_fbo(package)
                shipment = 0            

            # Тест
            print(f'cost_row is: {cost_row}')
            print(f'fbso is: {fbso}')
            print(f'logistics is: {logistics}')
            print(f'shipment is: {shipment}')

            # Запаковываем
            calcdata = self.calcdata_oz(
                cost_row = cost_row,
                des_profit = des_profit,
                logistics = logistics,
                cperc = cperc,
                risk = risk,
                tax_percent = tax_percent,
                cost_box = cost_box,
                wage = wage,
                shipment = shipment
            )

            # Отправляем на расчет           
            result = self._oz_calculate(tab, calcdata)
            results.append(result)

        # answer="OZPRICE_request"

        return results


    def ozprofit_request(self, stuff):

        answer="OZSPROFIT_request"

        return answer


    def _oz_calculate(self, tab, calcdata):
        """
        Логика нахождения цены OZON

        :param tab:
        :param calcdata:

        :return:
        """
        # ЛОГ
        logging.info(
            f'{Fore.GREEN}[ozcalc.py][oz_calculate]{Style.RESET_ALL}'
        )
        # Условия
        tolerance = 0.1
        max_iterations = 1000
        # Ожидаемый профит
        des_profit = float(calcdata.des_profit)
        # Начальное приближение
        price = (
            (calcdata.cost_row + calcdata.logistics + float(calcdata.shipment)
            + float(calcdata.wage) + float(calcdata.cost_box))
            * (1 + (float(calcdata.cperc) / 100))
        )
        # Тест
        logging.info(f'tab: {tab}')
        # Расчет
        for i in range(1, max_iterations):

            if tab == 'OZsole':
                price = self._price_calc_sole(calcdata, price)
                profit = self._profit_calc_sole(calcdata, price)

            elif tab == 'OZltd':
                price = self._price_calc_ltd(calcdata, price)
                profit = self._profit_calc_ltd(calcdata, price)

            else:
                logging.info(
                    f'{Fore.RED}[ozcalc.py][oz_calculate] TabError')
                break

            # Сраниваем
            diff = abs(profit - des_profit)

            if diff <= tolerance:
                return round(price)

        logging.info(f'{Fore.RED}Не удалось найти решение{Style.RESET_ALL}')
        return 0



    def _price_calc_sole(self, calcdata, price):
        """
        Расчет цены для OZON OOO

        :param calcdata: именованный кортеж со значениеями полей
        :param price: начальное приближение цены

        :return: цена
        """
        # ЛОГ
        logging.info(
            f'{Fore.GREEN}[ozcalc.py][price_calc_sole]'
        )
        # Последняя миля 
        lastmile = self._lastmile(price) 
        # Расчет комиссий
        comissions = price * (float(calcdata.cperc) / 100)
        tax = price * (float(calcdata.tax_percent) / 100)
        risk = price * (float(calcdata.risk) / 100) 
        # Все расходы
        all_costs = calcdata.cost_row + calcdata.logistics + float(calcdata.wage) + float(calcdata.cost_box) + lastmile + comissions + tax + risk 
        # Цена
        price = all_costs + calcdata.des_profit

        return price


    def _profit_calc_sole(self, calcdata, price):
        """
        Расчет профита для OZON OOO

        :param calcdata: именованный кортеж со значениеями полей
        :param price: начальное приближение цены

        :return: цена
        """
        # ЛОГ
        logging.info(
            f'{Fore.GREEN}[ozcalc.py][profit_calc_sole]'
        )
        # Последняя миля 
        lastmile = self._lastmile(price) 
        # Расчет комиссий
        comissions = price * (float(calcdata.cperc) / 100)
        tax = price * (float(calcdata.tax_percent) / 100)
        risk = price * (float(calcdata.risk) / 100) 
        # Все расходы
        all_costs = calcdata.cost_row + calcdata.logistics + float(calcdata.wage) + float(calcdata.cost_box) + lastmile + comissions + tax + risk 
        # Цена
        profit = price - all_costs
        
        return profit


    def _price_calc_ltd(self):
        pass 


    def _profit_calc_ltd(self):
        pass


    def _pack_size(self, package):
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


    def _logistics_oz_fbs(self, package):
        """
        Считаем цену логистики в зависимости
        от объема упаковки (9 руб для FBS)

        :param package: объем в литрах

        :return: цена
        """
        if package < 5:
            result = 76
        elif package > 5:
            factor = 9
            result = 76 + (math.ceil(package - 5) * 9)

        return result


    def _logistics_oz_fbo(self, package):
        """
        Считаем цену логистики в зависимости
        от объема упаковки (7 руб для FBO)
        Коэффициент локализации: 0.51

        :param package: объем в литрах

        :return: цена
        """
        if package < 5:
            result = 63
        elif package > 5:
            factor = 7
            result = 63 + (math.ceil(package - 5) * 9)

        result = result * 0.51

        return result


    def _lastmile(self, price):
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
