# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
class Solution(object):
    def generateParenthesis(self, n):
        if n == 1:
            return ['()']
        last_list = self.generateParenthesis(n - 1)
        res = []
        for t in last_list:
            curr = f'{t})'
            res.extend(
                f'{curr[:index]}({curr[index:]}'
                for index in range(len(curr))
                if curr[index] == ')'
            )
        return list(set(res))


    # def generateParenthesis(self, n):
    #     def generate(leftnum, rightnum, s, result):
    #         if leftnum == 0 and rightnum == 0:
    #             result.append(s)
    #         if leftnum > 0:
    #             generate(leftnum - 1, rightnum, s + '(', result)
    #         if rightnum > 0 and leftnum < rightnum:
    #             generate(leftnum, rightnum - 1, s + ')', result)
    #
    #     result = []
    #     s = ''
    #     generate(n, n, s, result)
    #     return result
