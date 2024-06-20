class WBCalcTest():


    def __init__(self):
        self.lastmile_factor = 0.055


    def lastmile(self, price):
        """ 
        ТЕСТ Считем последнюю милю OZON
        5.5% от цены, но не больше 500 руб

        :param price: 
        """
        lastmile_price = price * self.lastmile_factor

        if lastmile_price >= 500:
            lastmile_price = 500 
                    
        return lastmile_price


list_price = [
    9091,
    4000,
    6020,
    8700,
    10452,
    15087,
    60460,
]

calc = WBCalcTest() 

for i in list_price:
    lastmile_price = calc.lastmile(i)
    print(f'Цена товара: {i}\n Последняя миля: {lastmile_price}')


    
