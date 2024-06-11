from flask import request
from calculon_app.calculator.wbcalc import WBCalc
from calculon_app.calculator.ozcalc import OZCalc


class Calculon(WBCalc, OZCalc):


    def __init__(self):
        pass


    def entry_point(self, tab, subtab, formdata):
        """ 
        Первичная маршрутизация
        """
        # Тест
        # result = 'hello, it works!'
        print(f'tab is:{tab}, subtab is:{subtab}')
        print(f'formdata is: {formdata}')
        # Маршрутизация на переупаковку
        if subtab == 'Price':
            stuff = self.price_repack(formdata)
        elif subtab == 'Profit':
            result = self.profit_repack(tab, subtab, formdata)
        else: 
            print('Subtab error')

        # Отдаем словарь на расчеты 
        result = self.routing(tab, subtab, stuff) 
        
        return result
 

    def price_repack(self, formdata):
        """ 
        Переупаковка для дальнейшей маршрутизации.
        Вкладка Price.

        :param formdata: данные полей input

        :return: словаль товаров stuff
        """
        # Создаем словарь комплектов 
        stuff = {}

        # Упаковываем
        for count, wage, cost_box, size, in zip(
            request.form.getlist('count'), 
            request.form.getlist('wage'), 
            request.form.getlist('cost_box'), 
            request.form.getlist('box_size')
        ):
                stuff[count] = [
                wage, 
                cost_box, 
                size, 
                request.form.get('des_percent'), 
                request.form.get('cperc'), 
                request.form.get('tax'), 
                request.form.get('risk'), 
                request.form.get('cost_per_one'), 
                request.form.get('shipment'),
                request.form.get('fbsfbo_button')
            ]

        # Проверяем созданный словарь 
        for count, values in stuff.items():
            print(count, ":", values)
        
        # result = 'PRICE REPACK'
        return stuff


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
            "WBsole": {"Price": self.wbprice_request, "Profit": self.wbprofit_request},
            "WBltd": {"Price": self.wbprice_request, "Profit": self.wbprofit_request},
            "OZsole": {"Price": self.ozprice_request, "Profit": self.ozprofit_request},
            "OZltd": {"Price": self.ozprice_request, "Profit": self.ozprofit_request}
        }

        return methods.get(tab, {}).get(subtab, None)
    


