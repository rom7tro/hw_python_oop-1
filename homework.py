import datetime as dt
from typing import List, Any

records = []

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        now = dt.datetime.now()
        if self.date == None:
            self.date = now.date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
    def __str__(self):
        return " " + str(self.amount) + " " + self.comment + ' ' + str(self.date)

class Calculator():
    limit = 0
    records = []
    def __init__(self, limit=0):
        self.limit = limit

    def add_record(self):
        records.append(self)
    def __str__(self):
        return ' ' + str(self.limit) + str(records[0])


r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")
records = [r1, r2, r3, r4, r5, r6]
Calculator.add_record(Record(100, "Кулич"))
Calculator.add_record(Record(1000, "Куличчч"))
print(r2)
print(records[0].date)
print(str(records[0]))
print([print(i.amount, i.date) for i in records])
print(type(records[3].date))
