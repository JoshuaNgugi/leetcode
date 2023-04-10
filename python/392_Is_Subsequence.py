class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for a in s:
            if a not in t:
                return(False)
            for b in range(len(t)):
                if a==t[b]:
                    t=t[b+1:]
                    break
        return(True)
