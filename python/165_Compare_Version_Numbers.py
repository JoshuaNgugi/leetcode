class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=list(map(int,version1.split('.')))
        l2=list(map(int,version2.split('.')))
        if l1==l2:
            return(0)

        a=len(l1)
        b=len(l2)

        if a>b:
            l2.extend("0" for _ in range(a-b))
        else:
            l1.extend("0" for _ in range(b-a))
        for i in range(len(l1)):
            if int(l1[i])>int(l2[i]):
                return(1)

            elif int(l1[i])<int(l2[i]):
                return(-1)

        return(0)
