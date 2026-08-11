class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_hash = {}
        for word in sorted(strs):
            sorted_word = "".join(sorted(word))
            sorted_word_hash[sorted_word] = sorted_word_hash.get(sorted_word,[]) + [word]
        return [item[1] for item in sorted_word_hash.items()]


        
        