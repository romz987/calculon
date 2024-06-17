class WBCalc():


    def wbprice_request(self, stuff, tab):
        """
        Считаем цену для Wildberries ИП
        """
        return answer


    def wbsprofit_request(self, stuff):

        answer="WBSPROFIT_request"

        return answer


    def wblprofit_request(self, stuff):

        answer="WBLPROFIT_request"

        return answer


    def __pack_size(self, package):
        """
        Объем упаковки из строки вида "11*10*8"

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


    def __logistics_wb(self, package):
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


