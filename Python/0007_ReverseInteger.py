class Solution:
    # Solution 1 - Using Div, Mod
    def reverse(self, x: int) -> int:
        stack = []
        sign = -1 if x < 0 else 1
        x = abs(x)
        # for example, x is 523 then stack is [3, 2, 5]
        while x > 0:
            x, r = divmod(x, 10)
            stack.append(r)

        # given stack = [3, 2, 5]
        # this loop end up with 3 * (10^2) + 2 * (10^1) + 5 * (10^0)
        # which is 325
        # also works well with leading 0(s)
        re = 0
        for idx in range(len(stack)):
            re += stack[idx] * 10 ** (len(stack) - idx - 1)
        re = re * sign
        return re if -pow(2, 31) <= re <= pow(2, 31) - 1 else 0
