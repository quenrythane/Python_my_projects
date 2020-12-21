
# Zadanie 1
'''
user_number = input("podaj swój numer")
user_number.replace(" ","")
user_number.replace("-","")

for digit in range(10):
    digit_times_in_number = user_number.count(str(digit))
    if digit_times_in_number > 0:
        print(f"Cyfra {digit} występuje w Twoim numerze: {digit_times_in_number} razy")
'''

# Zadanie 2 Napisz kalkulator dla kredytu o malejącej racie
capital = int(input("Na jaką kwotę jest kredyt? "))
interest_rate = float(input("Jakie jest oprocentowanie (%)? "))
years = int(input("Na ile lat jest kredyt? "))
initial_fees = int(input("Jakie są koszty początkowe? "))

credit_time_in_months = years * 12
monthly_paid_capital = capital / credit_time_in_months
total_paid = initial_fees
for month_number in range(1, credit_time_in_months + 1):
    capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
    installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Rata w miesiącu {month_number} wyniesie {installment:.2f}")

print(f"Zaciągając {capital} na tych warunkach spłacisz z odsetkami {total_paid}")

