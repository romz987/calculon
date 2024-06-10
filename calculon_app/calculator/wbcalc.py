from collections import namedtuple


class WBCalc():


    # Используем именованный кортеж
    calcdata_strct = namedtuple('calcdata_strct', [
        'cost_row',
        'des_profit',
        'logistics',
        'cperc',
        'risk',
        'tax_percent',
        'cfix',
        'cost_box',
        'wage'
    ])


    def wbprice_request(self, stuff, tab):
        """
        Считаем цену для Wildberries ИП
        """
        # Тест
        print(f'I got it! Stuff is: {stuff}')
        # Начинаем расчеты для каждого комплекта
        for count, (
            wage, 
            cost_box, 
            package, 
            des_percent, 
            cperc, 
            cfix, 
            tax_percent, 
            risk,
            cost_per_one
        ) in stuff.items():

            # Себестоимость
            cost_row = int(count) * float(cost_per_one)
            des_profit = cost_row * (float(des_percent) / 100)
            # Логистика
            package = self._pack_size(package)  
            logistics = self._logistics_wb(package)

            # Тест
            print(f'cost_row is: {cost_row}')
            print(f'package is: {package}')
            print(f'logistics is: {logistics}')
            print(f'tab is {tab}')

            # Запаковываем
            calcdata = self.calcdata_strct(
                cost_row = cost_row,
                des_profit = des_profit,
                logistics = logistics,
                cperc = cperc,
                risk = risk,
                tax_percent = tax_percent,
                cfix = cfix,
                cost_box = cost_box,
                wage = wage
            )

            # Отправляем на расчет
            result = self._wb_calculate(tab, calcdata)


        answer="WBSPRICE_request"    
        return answer


    def wbprofit_request(self, stuff):

        answer="WBSPROFIT_request"

        return answer


    def _wb_calculate(self, tab, calcdata):
        """ 
        Логика нахождения цены
        """
        # Условия
        tolerance = 0.1
        max_iterations = 5

        # Ожидаемый профит
        des_profit = float(calcdata.des_profit)

        # Начальное приближение
        price = (
            (calcdata.cost_row + calcdata.logistics
            + float(calcdata.wage) + float(calcdata.cost_box))
            * (1 + (float(calcdata.cperc) / 100))
        )

        print(f'price is: {price}')

        for i in range(1, max_iterations):

            if tab == 'WBsole':
                price = self._price_calc_sole(calcdata, price)
                profit = self._profit_calc_sole(calcdata, price)

            elif tab == 'WBltd':
                price = self._price_calc_ltd(calcdata, price)
                profit = self._profit_calc_ltd(calcdata, price)

            else:
                print('TabError')
                break

            # Сраниваем
            diff = abs(profit - des_profit)

            if diff <= tolerance:
                break 

            if i >= max_iterations:
                print('Не удалось найти решение')
                price = 0 
                break

        return price


    def _price_calc_sole(self, calcdata, price):
        """ 
        Считает цену для WB ИП

        :param calcdata: именованный кортеж со значениями полей
        :param price: начальное приближение цены

        :return: price
        """
        print(f'we in _price_calc_sole method')

        # Комиссии, налоги, риски
        comissions = price * (float(calcdata.cperc) / 100)
        tax = price * (float(calcdata.tax_percent) / 100)
        risk = price * (float(calcdata.risk) / 100)
        # Все расходы
        all_costs = comissions + calcdata.logistics + float(calcdata.cost_box) + float(calcdata.wage) + risk + tax
        # Цена
        price = all_costs + calcdata.des_profit

        return price


    def _profit_calc_sole(self, calcdata, price):
        """ 
        Считает профит для WB ИП

        :param calcdata:  именованный кортеж со значениями полей
        :param price: рассчитанная в _price_calc_sole цена
        """
        print(f'we in _profit_calc_sole method')

        # Комиссии, налоги, риски
        comissions = price * (float(calcdata.cperc) / 100)
        tax = price * (float(calcdata.tax_percent) / 100)
        risk = price * (float(calcdata.risk) / 100)
        # Все расходы
        all_costs = comissions + calcdata.logistics + float(calcdata.cost_box) + float(calcdata.wage) + risk + tax
        # Профит
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


    def _logistics_wb(self, package):
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



