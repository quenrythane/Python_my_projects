def is_anagram(word1, word2):
    i = len(word2) - 1
    for letter in word1:
        if letter != word2[i]:
            return False
        i -= 1
    return True


print(is_anagram("kajak", "kajak"))
