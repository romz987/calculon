import math


class WBCalcTest():


    def __init__(self):
            # Логистика
            self.logistics_base_price = 30
            self.logistics_factor_min = 5
            self.logistics_factor_max = 6
            self.territorial_distrib_coeff = 1 


    def logistics_wb(self, volume_lt: float) -> float:
        """
        Цена упаковки в зависимости от объема упаковки
        в литрах.

        :param package: объем в литрах
        :return: цена
        """
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


volume_list = [
    0,
    0.01,
    0.1,
    0.99,
    0.999,
    1,
    1.1,
    1.99,
    2,
    2.1,
    5,
    5.1,
    5.99,
    6,
    6.99,
    7
]

log = WBCalcTest()

for volume_lt in volume_list:
    print(f'Объем: {volume_lt}')
    logistics = log.logistics_wb(volume_lt)
    print(f'Логистика: {logistics}\n')


