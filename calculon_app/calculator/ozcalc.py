import math 


class OZCalc():


    def __logistics_wb(self, volume_lt: float) -> float:
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
