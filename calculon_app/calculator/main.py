from flask import request
from calculon_app.calculator.wbcalc import WBCalc
from calculon_app.calculator.ozcalc import OZCalc
from calculon_app.calculator.logs import LogClass 


class Calculon(WBCalc, OZCalc, LogClass):


    def __init__(self):
        # STATIC
        self.comission_percent = 0
        self.tax_percent = 0
        self.risk_percent = 0
        self.profit_percent = 0    
        self.cost_per_one = 0
        self.profit_percent = 0
        # Ozon ONLY 
        self.shipment = 0
        self.lastmile = 0
        # DYNAMIC
        self.row_cost = 0
        self.wage_cost = 0
        self.box_cost = 0
        self.package_size = 0
        self.package_volume_lt = 0
        self.logistics = 0
        # Ozon ONLY
        self.lastmile = 0


    def var_reset_all(self):
        # STATIC
        self.comission_percent = 0
        self.tax_percent = 0
        self.risk_percent = 0
        self.profit_percent = 0    
        self.cost_per_one = 0
        self.profit_percent = 0
        # Ozon ONLY 
        self.shipment = 0
        self.lastmile = 0
        # DYNAMIC
        self.row_cost = 0
        self.wage_cost = 0
        self.box_cost = 0
        self.package_size = 0
        self.package_volume_lt = 0
        self.logistics = 0
        

    def var_reset_dynamic(self):
        # DYNAMIC
        self.row_cost = 0
        self.wage_cost = 0
        self.box_cost = 0
        self.package_size = 0
        self.package_volume_lt = 0
        self.logistics = 0
  

    def __pack_volume_lt(self, package_size: str) -> float:
        """
        Объем упаковки из строки вида "11*10*8"

        :param package_size: размер упаковки в см
        :return: объем в литрах
        """
        self.info_mesg('main.py','__pack_volume_lt', 'OK')
        # Преобразуем каждую часть строки в целое число
        numbers = map(int, package_size.split('*'))          
        result = 1
        for number in numbers:
            result *= number
       
        volume_lt = result / 1000

        return volume_lt





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


    


