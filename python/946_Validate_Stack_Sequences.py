class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        in_stack = []
        pos = 0
        while pos != len(pushed):
            curr = pushed[pos]
            while in_stack and len(popped) > 0 and in_stack[-1] == popped[0]:
                in_stack.pop(-1)
                popped.pop(0)
            if len(popped) == 0:
                break
            if curr == popped[0]:
                popped.pop(0)
            else:
                in_stack.append(curr)
            pos += 1
        while in_stack and len(popped) > 0 and in_stack[-1] == popped[0]:
            in_stack.pop(-1)
            popped.pop(0)
        return not in_stack


if __name__ == '__main__':
    s = Solution()
    # print s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    # print s.validateStackSequences([2, 1, 0], [1, 2, 0])
    print s.validateStackSequences([1, 0, 3, 2], [0, 1, 2, 3])
