from flask import request
from calculon_app.calculator.wbcalc import WBCalc
from calculon_app.calculator.ozcalc import OZCalc


class Calculon(WBCalc, OZCalc):


    def __init__(self):
        self.row_cost = 0
        self.box_cost = 0
        self.wage_cost = 0
        self.shipment = 0
        self.comission_percent = 0
        self.tax_percent = 0
        self.risk_percent = 0
        self.profit_percent = 0
        self.package = 0
        self.logistics = 0
        self.lastmile = 0


    def var_reset(self):
        self.row_cost = 0
        self.box_cost = 0
        self.wage_cost = 0
        self.shipment = 0
        self.comission_percent = 0
        self.tax_percent = 0
        self.risk_percent = 0
        self.profit_percent = 0
        self.package = 0
        self.logistics = 0
        self.lastmile = 0


    def entry_point(self, tab, subtab, formdata):
        """ 
        Первичная маршрутизация
        """
        # Тест
        # result = 'hello, it works!'
        print(f'tab is:{tab}, subtab is:{subtab}')

        # Маршрутизация на переупаковку
        if subtab == 'Price':
            result = self.price_repack(tab, subtab, formdata)
        elif subtab == 'Profit':
            result = self.profit_repack(tab, subtab, formdata)
        else: 
            print('Subtab error')
        
        return result
 

    def price_repack(self, tab, subtab, formdata):
        """ 
        Переупаковка для вкладки Price
        **(переработать)
        """
        # Создаем словарь комплектов 
        stuff = {}

        # Комплекты
        count = request.form.getlist('count')
        print(count)
        wage = request.form.getlist('wage')
        print(wage)
        cost_box = request.form.getlist('cost_box')
        print(cost_box)
        box_size = request.form.getlist('box_size')
        print(box_size)

        # Остальное
        des_percent = request.form.get('des_percent')    
        print(f'des_percent is: {des_percent}')

        cperc = request.form.get('cperc')
        print(f'cperc is: {cperc}')

        cfix = request.form.get('cfix')
        print(f'cfix is: {cfix}')
       
        tax_percent = request.form.get('tax')
        print(f'tax is: {tax_percent}')
       
        risk = request.form.get('risk')
        print(f'risk is: {risk}')

        cost_per_one = request.form.get('cost_per_one')
        print(f'cost_per_one is: {cost_per_one}')


        # Создаем словарь
        for count, wage, cost, size, in zip(count, wage, cost_box, box_size):
            stuff[count] = [wage, cost, size, des_percent, cperc, cfix, tax_percent, risk, cost_per_one]

        # Проверяем созданный словарь 
        for count, values in stuff.items():
            print(count, ":", values)

        # Отдаем словарь на расчеты 
        result = self.routing(tab, subtab, stuff) 
        
        # result = 'PRICE REPACK'
        return result


    def profit_repack(self, tab, subtab, formdata):
        """ 
        Переупаковка для вкладки Profit
        """
        result = 'profit_repack'

        return result 


    def routing(self, tab, subtab, stuff):
        """  
        Роутинг на метод

        :param tab:
        :param subtab:
        :param stuff:

        :return: 
        """
        # Оборачиваем
        method = self.get_method(tab, subtab)

        # Вызываем
        if method:
            result = method(stuff, tab)
        else:
            print('Error in tab or subtab')
            result = 'No such func'

        return result


    def get_method(self, tab, subtab):
        """
        Словарь методов

        :return:
        """
        methods = {
            "WBsole": {"Price": self.wbprice_request, "Profit": self.wbsprofit_request},
            "WBltd": {"Price": self.wbprice_request, "Profit": self.wblprofit_request},
            "OZsole": {"Price": self.ozprice_request, "Profit": self.ozsprofit_request},
            "OZltd": {"Price": self.ozprice_request, "Profit": self.ozlprofit_request}
        }

        return methods.get(tab, {}).get(subtab, None)


    


