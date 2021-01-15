letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q' 'r',
           's', 'ś', 't', 'u', 'v', 'w', 'x', 'x', 'y', 'z', 'ż', 'ź']

help = """Szyfr Cezara jest to proste szyfrowanie używane przez samego Cezara
Działa on tak, że zamienia obecną literę na inną przesunietą o wartośćkroku.
Przykład:
litera 'a' jest pierwszą literą alfabetu. Jeśli zadamy krok = 3 to zamienimy
ją na literę czwartą z alfabetu (1 + 3 = 4),  a więc literę d.
Według tej zasady kodujemy wszystkie litery
"""


def code_message(message, step):
    coded_message = ""
    for sign in message:
        if sign not in letters:
            coded_message += sign
            continue
        i = letters.index(sign) + step
        if i >= len(letters):
            i -= len(letters)
        coded_message += letters[i]
    print('zakodowana wiadomość:', coded_message)


def uncode_message(message, step):
    uncoded_message = ""
    for sign in message:
        if sign not in letters:
            uncoded_message += sign
            continue
        i = letters.index(sign) - step
        uncoded_message += letters[i]
    print('odkodowana wiadomość:', uncoded_message)


print("""
Witam cię w maszynie kodującej i dekodującej szyfr Cezara
Jeśli nie wiesz jak to działą użyj komendy 'pomoc'.
Jeśli chcesz skorzystać z kodowania wpisz komendę:
'zakoduj' lub 'odkoduj'
a następnie podaj tekst wiadomości oraz krok szyfru
""")
exit = ""
while exit != 'exit':
    print('żeby zakończyć napisz "exit"')
    what_to_do = input("czego potrzebujesz?: zakoduj / odkoduj / pomoc: ")
    exit = what_to_do

    if what_to_do == "exit":
        print("dzięki za zabawę!")

    elif what_to_do == "pomoc":
        print(help)

    elif what_to_do == "zakoduj":
        message = input('podaj wiadomość: ').lower()
        step = int(input('podaj krok: '))
        code_message(message, step)

    elif what_to_do == "odkoduj":
        message = input('podaj wiadomość: ').lower()
        step = int(input('podaj krok: '))
        uncode_message(message, step)

    else:
        print("Wystąpił niespodziewany błąd. Spróbuj raz jeszcze")
