
# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word1 = sorted(word.lower())
    word2 = sorted(anagram.lower())
    if (word1 == word2):
        return True
    return False


print(find_anagram('below', 'elbow'))
