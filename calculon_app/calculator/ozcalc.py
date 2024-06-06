import math 


class OZCalc():

    
    def ozprice_request(self, stuff):

        print(f'I got it! Stuff is: {stuff}')

        answer="OZSPRICE_request"

        return answer


    def ozsprofit_request(self, stuff):

        answer="OZSPROFIT_request"

        return answer


    def ozlprofit_request(self, stuff):

        answer="OZLPROFIT_request"

        return answer


    def _oz_calculate(self):
        pass 


    def _price_calc_sole(self):
        pass 


    def _profit_calc_sole(self):
        pass 


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


    def _logistics_oz(self, package):
        """
        Считаем цену логистики в зависимости

        от объема упаковки

        :param package: объем в литрах

        :return: цена
        """
        if package < 5:
            result = 76
        elif package > 5:
            factor = 9
            result = 76 + (math.ceil(package - 5) * 9)

        return result


    def _lastmile(price):
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
