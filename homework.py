import datetime as dt


class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        self.date = date
        now = dt.datetime.now()
        if self.date == None:
            self.date = now.date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()

        def __str__(self):
            return str(self.amount)

class Calculator():
    limit = 0
    arg = None
    records = []

    def __init__(self, limit):
        self.limit = limit

    def add_record(self, arg):
        self.records.append(arg)

    def get_today_stats(self):
        count_now = 0                                  # Счетчик количества "удавов" за сегодняшний день
        for record in self.records:
            if record.date == dt.datetime.now().date():
                count_now += record.amount
        return count_now

    def get_today_remained(self):
        limit_now = self.limit
        for i in self.records:                               # Счетчик остатка "удавов" от лимита за сегодняшний день
            if i.date == dt.datetime.now().date():
                limit_now -= i.amount
        return limit_now

    def get_week_stats(self):
        week_days = []
        count_week_days = 0
        for i in range(6):
            week_days.append((dt.datetime.now() - dt.timedelta(days = i)).date())   # Добавляет в список дни прошедшей
                                                                                    # недели
        for i in self.records:
            if i.date in week_days:
                count_week_days += i.amount                                         # Счетчик количества "удавов"
        return count_week_days                                                      # за неделю
class CaloriesCalculator(Calculator):

    records = []

    def get_calories_remained(self):
        limit_now = super().get_today_remained()
        if (self.limit - limit_now) < 0:
            return 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' +\
                   str(limit_now) +' кКал'
        else:
            return 'Хватит есть!'
    def get_today_stats(self):
        return ("Сегодня вы потратили " + str(super().get_today_stats()) + "кКал")

    def get_week_stats(self):
        return ("За неделю вы потратили " + str(super().get_week_stats()) + " кКал")

class CashCalculator(Calculator):
    records = []
    RUB_RATE = 1
    USD_RATE = 1/80
    EURO_RATE = 1/90
    dict_currency ={'rub': ' руб.', 'usd': ' долларов', 'eur': ' евро'}
    rate_currency = {'rub': RUB_RATE, 'usd': USD_RATE, 'eur': EURO_RATE}

    def get_today_cash_remained(self, currency):
        today_cash_remained = self.get_today_remained()
        dict_solut = self.dict_currency[currency]
        if today_cash_remained > 0:
            return 'На сегодня осталось ' \
                   + str(round(today_cash_remained*self.rate_currency[currency], 2)) + str(dict_solut)
        elif today_cash_remained < 0:
            return 'Денег нет, держись: твой долг - ' \
                   + str(abs(round(today_cash_remained*self.rate_currency[currency], 2))) + str(dict_solut)
        else:
            return 'Денег нет'

    def get_today_stats_(self):
        return 'За сегодня вы потратили ' + str(super().get_today_stats()) + ' руб.'

    def get_week_stats(self):
        return 'За неделю вы потратили ' + str(super().get_week_stats()) + ' руб.'

if __name__ == '__main__':
    calories_calculator = CaloriesCalculator(1000)
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="Безудержный шопинг", date="31.01.2022"))
    cash_calculator.add_record(Record(amount=1568, comment="Наполнение потребительской корзины", date="30.03.2022"))
    cash_calculator.add_record(Record(amount=691, comment="Катание на такси", date="22.01.2022"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="30.01.2022"))
    calories_calculator.add_record(Record(amount=1186, comment="Кусок тортика. И ещё один.", date="31.01.2022"))
    calories_calculator.add_record(Record(amount=84, comment="Йогурт.", date="31.01.2022"))
    calories_calculator.add_record(Record(amount=1140, comment="Баночка чипсов.", date="29.01.2022"))

    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_stats_())
    print(cash_calculator.get_week_stats())
    print()
    print(calories_calculator.get_calories_remained())
    print(calories_calculator.get_today_stats())
    print(calories_calculator.get_week_stats())