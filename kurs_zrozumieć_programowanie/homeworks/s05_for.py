# Zadanie 1
'''
grades = []
print("Python zapyta Cię o podanie ocen, z których wyliczy śrędnią. \nPo wprowadzniu wszystkich ocen wpisz 'X' żeby obliczył średnią")
grade_input = input("Podaj ocenę: ")
while grade_input != 'X' and grade_input != 'x' :
    grade = float(grade_input)
    grades.append(grade)
    grade_input = input("Podaj kolejną ocenę: ")

grades_sum = 0
grades_sum = 0
for grade in grades:
    grades_sum += grade

average = grades_sum / len(grades)
print(f"Twoja średnia wynosi: {average:.2f}")
if average >= 4.75:
    print("Gratuluje!")
'''

# Zadanie 2
'''
# przyjęcie od użytkownika numeru oraz usunięcia z niego zbędnych znaków (spacji i myślników)
user_number = input("wpisz swój numer telefonu: ")
user_number = user_number.replace("-", "")
user_number = user_number.replace(" ", "")

# sprawdzenie czy numer użytkownika ma prawidłową długość
while len(user_number) != 9:
    print("Twój numer ma nieprawidłową długość. Powinien liczyć 9 cyfr")
    user_number = input("wpisz poprawny numer telefonu: ")
    user_number = user_number.replace("-", "")
    user_number = user_number.replace(" ", "")

new_number = ""
for index, digit in enumerate(user_number):
    if index % 3 == 0 and index != 0:
        new_number += '-'
    new_number += digit
print(new_number)
'''

#Zadanie 3
'''
expenditures = {}
print("Phyton zapyta Cię o wprowadzenie kategorii wydatków oraz dokonane w nich wydatki")
print("Kiedy wprowadzisz wszystkei wydatki wpisz 'x' żeby je zatwierdzić")

category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
while category_name != 'x' and category_name != 'X':
    expenditures[category_name] = []
    expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    while expenditure != 'X' and expenditure != 'x':
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")

total_expenditures = 0
for category_expenditures in expenditures.values():
    for expenditure_value in category_expenditures:
        total_expenditures += expenditure_value

expenditures_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = 0
    for expenditure_value in category_expenditures:
        total_category_expenditures += expenditure_value
    # total_category_expenditures = sum(category_expenditures)
    expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures

most_important_category = None
most_important_category_percentage = 0
for category, percentage in expenditures_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_category is not None:
    print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")

for category, percentage in expenditures_percentage.items():
    print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")
'''
