class WBCalc():


    def __init__(self):
        # Логистика
        self.logistics_base_price = 30
        self.logistics_factor_min = 5
        self.logistics_factor_max = 6
        self.territorial_distrib_coeff = 1 


    def wbprice_request(self):
        """
        Считаем цену для Wildberries ИП
        """
        return answer


    def wbprofit_request(self):

        answer="WBSPROFIT_request"

        return answer


    def __logistics_wb(self, volume_lt: float) -> float:
        """
        Цена упаковки в зависимости от объема упаковки
        в литрах.

        :param package: объем в литрах
        :return: цена
        """
        self.info_mesg('wbcalc.py','__logistics_wb','OK')

        if volume_lt <= 1:
            logistics = self.logistics_base_price

        elif volume_lt < 5:
            logistics = (
                (math.ceil(volume_lt - 1)) * self.logistics_factor_min + 
                self.logistics_base_price
            ) * self.territorial_distrib_coeff    

        elif volume_lt >= 5:
            logistics = (
                (math.ceil(volume_lt - 1)) * self.logistics_factor_max + 
                self.logistics_base_price
            ) * self.territorial_distrib_coeff

        return logistics

