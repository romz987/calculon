import math 


class OZCalc():


    def __init__(self):
        # Логистика
        self.logistics_base_price = 76
        self.logistics_factor = 9
        self.territorial_distrib_coeff = 1
        self.lastmile_factor = 0.055


    def __logistics_oz(self, volume_lt: float) -> float:
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


    def __lastmile(self, price):
        """ 
        Считем последнюю милю
        5.5% от цены, но не больше 500 руб

        :param price: 
        """
        lastmile_price = price * self.lastmile_factor

        if lastmile_price >= 500:
            lastmile_price = 500 
                    
        return lastmile_price

    
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
