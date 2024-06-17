class WbCalcTest:


    def pack_size(self, package):
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


    def logistics_wb(self, volume_lt):
        """
        Считаем цену логистики в зависимости
        от объема упаковки

        :param package: объем в литрах

        :return: цена
        """
        if volume_lt < 5:
            factor = 5
        else:
            factor = 6

        logistics = 30 + factor + factor * ((volume_lt - 0.01) // 1)

        return logistics



package_list = [
    '0*0*0',
    '1*0*0',
    '1*0*1',
    '1*1*1',
    '1*2*1',
    '8*8*8',
    '10*10*10',
    '11*10*9',
    '100*5*4'
]

log = WbCalcTest()

for i in package_list:
    volume_lt = log.pack_size(i)
    print(f'volume in lt is: {volume_lt}')

    logistics = log.logistics_wb(volume_lt)
    print(f'logistics price is: {logistics}\n\n')


