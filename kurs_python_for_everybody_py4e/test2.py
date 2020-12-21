# policz ilość słów i znajdź słowo które
# najczęściej się powtarza oraz liczbę powtórzeń
file_name = input("enter name of file: ")
if len(file_name) < 1:
    file_name = "test.txt"
file_handle = open(file_name)

dict_of_words = {}
for line in file_handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dict_of_words[word] = dict_of_words.get(word, 0) + 1

the_most_common_word = None
the_number_of_the_word = 0
for key, value in dict_of_words.items():
    if value == 0 or value > the_number_of_the_word:
        the_number_of_the_word = value
        the_most_common_word = key
print(the_most_common_word, the_number_of_the_word)

