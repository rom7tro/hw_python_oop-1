import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def get_week_stats(self):
        amount = 0
        now = dt.datetime.now().date()
        week_ago = now - dt.timedelta(days=7)
        for record in self.records:
            if week_ago <= record.date:
                amount += record.amount
        return amount

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        amount = 0
        now = dt.datetime.now().date()
        for record in self.records:
            if now == record.date:
                amount += record.amount
        return amount
    
class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        if  type(date) is str:
            date = dt.datetime.strptime(date, date_format).date()
        self.date = date

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, record):
        super().add_record(record)

    def get_today_stats(self):
        return super().get_today_stats()

    def get_week_stats(self):
        return super().get_week_stats()        

    def get_calories_remained(self):
        total_amount = self.get_today_stats()
        if total_amount < self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {:.0f} кКал'.format(self.limit - total_amount))
        elif total_amount >= self.limit:
            return (f'Хватит есть!')


class CashCalculator(Calculator):
    
    USD_RATE = 75.88
    EURO_RATE = 88.75

    def __init__(self, limit):
        super().__init__(limit)
    
    def add_record(self, record):
        super().add_record(record)
    
    def get_today_stats(self):
        return super().get_today_stats()

    def get_week_stats(self):
        return super().get_week_stats()

    
    def currency_change(self, amount, currency, USD_RATE, EURO_RATE):
        if currency == "usd":
            return amount / self.USD_RATE
        elif currency == "eur":
            return amount / self.EURO_RATE
        else:
            return amount

    def get_today_cash_remained(self, currency):
        currency_name = { "rub":"руб",
                          "usd":"USD",
                          "eur":"Euro" }
        total_amount = self.get_today_stats()
        if currency in currency_name:
            if total_amount < self.limit:
                return ('На сегодня осталось {:.2f}'.format(self.currency_change((self.limit - total_amount), currency, self.EURO_RATE, self.USD_RATE))
                 + " " + currency_name[currency])
            elif total_amount == self.limit:    
                return ('Денег нет, держись')
            else:      
                return ('Денег нет, держись: твой долг - {:.2f}'.format(self.currency_change((total_amount - self.limit), currency, self.EURO_RATE, self.USD_RATE)) 
                + " " + currency_name[currency])
    
   
