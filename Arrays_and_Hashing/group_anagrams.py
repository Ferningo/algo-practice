class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for word in strs:
            sorted_word = self.create_sorted_string(word)
            if result_dict.get(sorted_word, None) == None:
                result_dict[sorted_word] = [word]
            else:
                result_dict[sorted_word].append(word)

        result_array = []
        for key in result_dict:
            result_array.append(result_dict[key])

        return result_array

    def create_sorted_string(self, word):
        word = sorted(word)
        result = ""
        result = result.join(word)
        return result
