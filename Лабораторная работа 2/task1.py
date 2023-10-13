money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_of_months_without_debt = 0
current_budget = money_capital + salary

while spend < current_budget:
    current_budget -= spend
    current_budget += salary
    spend += spend * increase
    count_of_months_without_debt += 1
print("Количество месяцев, которое можно протянуть без долгов:", count_of_months_without_debt)
