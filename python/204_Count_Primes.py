class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        isPrime = [True] * n
        for i in xrange(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in xrange(i * i, n, i):
                isPrime[j] = False
        return sum(bool(isPrime[i]) for i in xrange(2, n))
