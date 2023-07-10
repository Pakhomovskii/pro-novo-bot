import requests

from database.database import get_user_budget, get_user_car_age, get_user_car_engine_capacity


class Currency:
    link = "https://www.cbr-xml-daily.ru/daily_json.js"

    def bank(self, link):
        link = Currency.link
        data = requests.get(link)
        forex = data.json()['Valute']
        return forex


class Euro(Currency):
    def __init__(self, euro):
        self.euro = euro

    def exchange_rub(self):
        bank = self.bank(Currency.link)
        rub = bank['EUR']['Value']
        return self.euro * rub


class CarTaxCalculator:
    def __init__(self, cost, age, power, capacity):
        self.cost = cost
        self.age = age
        self.power = power
        self.capacity = capacity

    async def calculate_tax(self):
        if self.age < 3:
            if self.cost < 8500:
                tax_rate = 0.54
                minimum_tax = 2.5
            elif self.cost < 16700:
                tax_rate = 0.48
                minimum_tax = 3.5
            elif self.cost < 42300:
                tax_rate = 0.48
                minimum_tax = 3.5
            elif self.cost < 84500:
                tax_rate = 0.48
                minimum_tax = 7.5
            elif self.cost < 169000:
                tax_rate = 0.48
                minimum_tax = 15
            else:
                tax_rate = 0.48
                minimum_tax = 20
        elif 3 <= self.age <= 5:
            minimum_tax = 1
            if self.capacity < 1000:
                tax_rate = 1.5
            elif self.capacity < 1500:
                tax_rate = 1.7
            elif self.capacity < 1800:
                tax_rate = 2.5
            elif self.capacity < 2300:
                tax_rate = 2.7
            elif self.capacity < 3000:
                tax_rate = 3
            else:
                tax_rate = 3.6
        else:
            minimum_tax = 1
            if self.capacity < 1000:
                tax_rate = 3
            elif self.capacity < 1500:
                tax_rate = 3.2
            elif self.capacity < 1800:
                tax_rate = 3.5
            elif self.capacity < 2300:
                tax_rate = 4.8
            elif self.capacity < 3000:
                tax_rate = 5
            else:
                tax_rate = 5.7

        tax = max((self.capacity * tax_rate), minimum_tax)
        return tax


async def calculate_sum(user_chat_id=None):
    cost = await get_user_budget(user_chat_id)
    age = await get_user_car_age(user_chat_id)
    capacity = await get_user_car_engine_capacity(user_chat_id)
    cost_int = int(cost[0][0])

    if age[0][0] == "меньше 3-х лет":
        age_int = 2
    if age[0][0] == "3-5 лет":
        age_int = 4
    if age[0][0] == "5-7 лет":
        age_int = 6
    if age[0][0] == "больше 7 лет":
        age_int = 8
    # else:
    #     age_int = None

    capacity_int = int(float(capacity[0][0]) * 1000)
    print(capacity_int)
    tax_for_new_car = CarTaxCalculator(cost=cost_int, age=age_int, power=0, capacity=capacity_int)
    # rate = Euro(1)
    print(int(await tax_for_new_car.calculate_tax()))

    tax = int(await tax_for_new_car.calculate_tax())

    return tax


async def get_euro():
    rate = Euro(1)
    return float(rate.exchange_rub())
