deposit = float(input("Введите сумму депозита:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = [percent*(deposit/100) for percent in per_cent.values()]
print('суммы, которые вы можете заработать =', money)
print('Максимальная сумма, которую вы можете заработать =', max(money))