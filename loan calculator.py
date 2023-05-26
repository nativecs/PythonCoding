year = 0
amount = 1000
interest  = 0.05
for year in range(10):
  amount = (amount * interest) + amount
  amount = round(amount, 2)
  print('total interest in year', year + 1, "is", amount)