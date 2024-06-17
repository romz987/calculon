class WBCalc():


    def wbprice_request(self):
        """
        Считаем цену для Wildberries ИП
        """
        return answer


    def wbprofit_request(self):

        answer="WBSPROFIT_request"

        return answer


    def __pack_size(self, package):
        """
        Объем упаковки из строки вида "11*10*8"

        :param package: строка с размером упаковки

        :return: объем в литрах
        """

        # Преобразуем каждую часть строки в целое число
        numbers = map(int, package.split('*'))          
        result = 1
        for number in numbers:
            result *= number
       
        volume_lt = result / 1000


        return volume_lt


    def __logistics_wb(self, volume_lt):
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

        logistics = 30 + factor + factor * ((package - 0.01) // 1)

        return logistics


