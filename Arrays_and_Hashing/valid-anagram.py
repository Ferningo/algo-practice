class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_word_dict = {}
        second_word_dict = {}
        for i in range(len(s)):
            self.add_to_dict(first_word_dict, s[i])
            self.add_to_dict(second_word_dict, t[i])
        for key in first_word_dict.keys():
            if first_word_dict[key] != second_word_dict.get(key, 0):
                return False
        return True

    def add_to_dict(self, my_dictionary: dict, letter):
        if letter not in my_dictionary.keys():
            my_dictionary[letter] = 1
        else:
            my_dictionary[letter] += 1
