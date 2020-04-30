import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def get_week_stats(self):
        now = dt.datetime.now().date()
        week_ago = now - dt.timedelta(days=7)
        amount = [record.amount for record in self.records if week_ago <= record.date ]
        return sum(amount)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        now = dt.datetime.now().date()
        amount = [record.amount for record in self.records if now == record.date ]
        return sum(amount)
    
class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if isinstance(date, str):
            date = dt.datetime.strptime(date, date_format).date()
        self.date = date

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total_amount = self.get_today_stats()
        if total_amount < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {(self.limit - total_amount):.0f} кКал'
        elif total_amount >= self.limit:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    
    USD_RATE = 75.88
    EURO_RATE = 88.75

    def get_today_cash_remained(self, currency):
        currency_name = { "rub": ["руб", 1],
                          "usd": ["USD", self.USD_RATE],
                          "eur": ["Euro", self.EURO_RATE] }
        total_amount = self.get_today_stats()
        if currency in currency_name:
            if total_amount < self.limit:
                return f'На сегодня осталось {(self.limit - total_amount)/currency_name[currency][1]:.2f} {currency_name[currency][0]}'            
            elif total_amount == self.limit:    
                return 'Денег нет, держись'
            else:      
                return f'Денег нет, держись: твой долг - {(total_amount - self.limit)/currency_name[currency][1]:.2f} {currency_name[currency][0]}'


