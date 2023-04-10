Morse_tab = [".-","-...","-.-.",
             "-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--",
             "-..-","-.--","--.."]

class Solution(object):
    # https://leetcode.com/problems/unique-morse-code-words/solution/
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        ans_set = {
            "".join(Morse_tab[ord(c) - ord('a')] for c in word) for word in words
        }
        return len(ans_set)
