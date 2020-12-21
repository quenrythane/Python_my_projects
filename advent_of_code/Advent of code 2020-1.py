"""
file = open("input.txt")
vector = []
for string in file:
    vector.append((int)(string.strip("\n")))
file.close()
def tak(list):
    for a in vector:
        for b in vector:
            for c in vector:
                if a + b + c == 2020:
                    return(a * b * c)

print(tak(vector))
"""


from functools import reduce

with open("input.txt", "r") as file:
    data = file.readlines()
    puzzle_import = [int(line.strip()) for line in data]

def findSumWithTwoNumbers(listOfNumbers, target):
    for num in listOfNumbers:
        if target - num in listOfNumbers:
            return (target - num) * num

def findSumWithThreeNumbers(listOfNumbers, target):
    for number in listOfNumbers:
        diff = target - number
        result = findSumWithTwoNumbers(listOfNumbers, diff)
        if result is not None:
            return number * result

print(findSumWithTwoNumbers(puzzle_import, 2020))
print(findSumWithThreeNumbers(puzzle_import, 2020))