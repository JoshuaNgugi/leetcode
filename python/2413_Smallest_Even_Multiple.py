class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
            n : positive integer
            return : smallest positive integer that is a multiple of both 2 and n
        """
        return n if n % 2 == 0 else n * 2
        
