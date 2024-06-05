from flask import request
# from calculon_app.calculator.calc_requests import CalculonRequests


class Calculon():


    def __init__(self):
        pass


    def entry_test(self, tab, subtab, formdata):
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
        Первичный расчет и переупаковка для вкладки Price
        """
        result = 'price_repack'
        
        return result


    def profit_repack(self, tab, subtab, formdata):
        """ 
        Первичный расчет и переупаковка для вкладки Profit
        """
        result = 'profit_repack'

        return result 


























    def get_method(self, tab, subtab):
        """
        Создаем словарь функций

        :return:
        """
        methods = {
            "WBsole": {"Price": self.wbsprice_request, "Profit": self.wbsprofit_request},
            "WBltd": {"Price": self.wblprice_request, "Profit": self.wblprofit_request},
            "OZsole": {"Price": self.ozsprice_request, "Profit": self.ozsprofit_request},
            "OZltd": {"Price": self.ozlprice_request, "Profit": self.ozlprofit_request}
        }

        return methods.get(tab, {}).get(subtab, None)


    def entry_point(self, tab, subtab, formdata):
        """  
        Точка входа

        :param tab:
        :param subtab:
        :param formdata:

        :return: строку результата 
        """
        # Тест получения данных из форм
        #print(tab)
        #print(subtab)
        #print(f'formdata is {formdata}')

        # Оборачиваем
        method = self.get_method(tab, subtab)

        # Вызываем
        if method:
            result = method(formdata)
        else:
            print('Error in tab or subtab')
            result = 'No such func'

        return result


