class WBCalc():


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


    def wbprice_request(self, stuff):
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
            # Логистика
            package = self._pack_size(package)  
            logistics = 0

            # Тест
            print(f'cost_row is: {cost_row}')
            print(f'package is: {package}')


        answer="WBSPRICE_request"    
        return answer


    def wbsprofit_request(self, stuff):

        answer="WBSPROFIT_request"

        return answer



    def wblprofit_request(self, stuff):

        answer="WBLPROFIT_request"

        return answer

