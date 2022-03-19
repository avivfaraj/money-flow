from flow.src.withdrawal import Withdrawal
from flow.src.deposit import Deposit
from datetime import datetime

first = Deposit(ID = 1, details = "Income from USAA", total = 4.5)
print(first)
print()
first = Withdrawal(ID = 1,
			 	details = "Bike shoes",
			 	date = datetime(2021, 2,4,5,6),
			 	unit_price = 4,
			 	amount = 5)
print(first)

