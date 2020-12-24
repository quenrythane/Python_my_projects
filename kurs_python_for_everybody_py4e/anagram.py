""" first verison
def is_anagram(word1, word2):
    for i, letter in enumerate(word1):
        if letter != word2[::-1]:
            return False
    return True


print(is_anagram("", "a"))
"""

def is_anagram(word1, word2): return word1[::-1] == word2


print(is_anagram("word", "drow"))
