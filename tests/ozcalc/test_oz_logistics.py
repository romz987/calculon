import math


class WBCalcTest():


    def __init__(self):
            # Логистика
            self.logistics_base_price = 76
            self.logistics_factor = 9
            self.territorial_distrib_coeff = 1 


    def logistics_wb(self, volume_lt: float) -> float:
        """
        ТЕСТ расчета цены логистики от объема упаковки
        OZON

        :param package: объем в литрах
        :return: цена
        """
        if volume_lt <= 5:
            logistics = self.logistics_base_price
 
        elif volume_lt > 5:
            logistics = (
                (math.ceil(volume_lt - 5)) * self.logistics_factor + 
                self.logistics_base_price
            ) * self.territorial_distrib_coeff

        else: 
            print('value error')

        return logistics


volume_list = [
    0,
    0.1,
    0.999,
    1,
    4.9,
    5,
    5.1,
    6,
    6.1,
    7,
    8,
    9,
    9.1
]

log = WBCalcTest()

for volume_lt in volume_list:
    print(f'Объем: {volume_lt}')
    logistics = log.logistics_wb(volume_lt)
    print(f'Логистика: {logistics}\n')


