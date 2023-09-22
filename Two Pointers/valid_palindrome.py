class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:

            while (self.isValidChar(s[i]) == False and i < j):
                i += 1

            while (self.isValidChar(s[j]) == False and j > i):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            if i == j and s[i-1].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        return True

    def isValidChar(self, my_char):
        return my_char.isalnum()
