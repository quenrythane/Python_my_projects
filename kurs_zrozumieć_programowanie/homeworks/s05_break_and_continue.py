# Zadanie 1
'''
grades = []
while True:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
    if grade_input == "X" or grade_input == "x" :
        break
    if grade_input == "1":
        sorry += 1
        print("Przykro mi ale jeśli masz jedynkę to nie możesz zdać do następnej klasy")
        break
    grade = int(grade_input)
    grades.append(grade)
if sorry == 0:
    grades_sum = sum(grades)
    average = grades_sum / len(grades)
    print(f"Twoja średnia wynosi: {average:.2f}")
'''

# Zadanie 2
'''
expenditures = {}
print("Phyton zapyta Cię o wprowadzenie kategorii wydatków oraz dokonane w nich wydatki")
print("Kiedy wprowadzisz wszystkei wydatki wpisz 'x' żeby je zatwierdzić")

while True:
    category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
    if category_name == 'x' or category_name == 'X':
        break
    expenditures[category_name] = []
    
    while True:
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
        if expenditure == 'X' or expenditure == 'x':
            break
            
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)

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

# Zadanie 3
'''
list = [1, 3, 4, 6, 7, 9, 0]
for number in list:
    if number % 2 == 0 or number == 0:
        continue
    print(number)
'''