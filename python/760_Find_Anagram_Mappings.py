class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        val_index = {n: i for i, n in enumerate(B)}
        return [val_index[n] for n in A]
