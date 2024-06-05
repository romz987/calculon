from flask import request
from calculon_app.calculator.wbcalc import WBCalc


class Calculon(WBCalc):


    def __init__(self):
        pass


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
        Первичный расчет и переупаковка для вкладки Price
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
        Первичный расчет и переупаковка для вкладки Profit
        """
        result = 'profit_repack'

        return result 


    def routing(self, tab, subtab, stuff):
        """  
        Точка входа

        :param tab:
        :param subtab:
        :param stuff:

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
            result = method(stuff)
        else:
            print('Error in tab or subtab')
            result = 'No such func'

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


    

    def ozsprice_request(self, stuff):

        print(f'I got it! Stuff is: {stuff}')

        answer="OZSPRICE_request"

        return answer


    def ozlprice_request(self, stuff):

        print(f'I got it! Stuff is: {stuff}')

        answer="OZLPRICE_request"

        return answer


    def ozsprofit_request(self, stuff):

        answer="OZSPROFIT_request"

        return answer


    def ozlprofit_request(self, stuff):

        answer="OZLPROFIT_request"

        return answer
