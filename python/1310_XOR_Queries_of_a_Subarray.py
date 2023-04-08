class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        # Compute accumulated xor from head
        pref.extend(e ^ pref[-1] for e in arr)
        return [pref[r+1] ^ pref[l] for [l, r] in queries]

    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     for i in range(len(arr) - 1):
    #         arr[i + 1] ^= arr[i]
    #     return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
