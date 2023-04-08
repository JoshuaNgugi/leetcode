class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dictionary = set(dictionary)
        self.abb_dic = {}
        for s in self.dictionary:
            curr = self.getAbb(s)
            self.abb_dic[curr] = curr not in self.abb_dic

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abb = self.getAbb(word)
        hasAbbr = self.abb_dic.get(abb, None)
        return hasAbbr is None or (hasAbbr and word in self.dictionary)


    def getAbb(self, word):
        return word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]



        # Your ValidWordAbbr object will be instantiated and called as such:
        # vwa = ValidWordAbbr(dictionary)
        # vwa.isUnique("word")
        # vwa.isUnique("anotherWord")