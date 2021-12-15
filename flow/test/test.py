from flow.src.income import Income
from flow.src.expense import Expense
from datetime import datetime

first = Income(ID = 1, details = "Income from USAA", salary = 4.5)
print(first)

first = Expense(ID = 1,
			 	details = "Bike shoes",
			 	date = datetime(2021, 2,4,5,6),
			 	unit_price = 4,
			 	amount = 5)
print(first)