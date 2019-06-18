class Solution:
    # 时间: O(n)
    # 空间: O(n)
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        str_bd = ''
        num_bd = ''
        for ch in s:
            # 遍历字符串过程中共有四种情况需要考虑

            # 1. 遇到数字
            # 需要注意的是可能会遇到多个数字连续，continue 用于处理这个情况
            if ch.isdigit():
                num_bd += ch
                continue
            # 走到这一步说明遇到的不是数字，此时如果有累积的乘的系数要入栈
            if num_bd:
                num_stack.append(int(num_bd))
                num_bd = ''

            # 2. 开括号
            # 目前累计的字符串入栈，并清空
            if ch == '[':
                str_stack.append(str_bd)
                str_bd = ''
            # 3. 闭括号
            # 出栈系数和字符串，用出栈字符串加系数乘累计的字符串得到重复后的字符串
            elif ch == ']':
                fac = num_stack.pop()
                tmp = str_stack.pop() + fac * str_bd
                str_bd = tmp
            # 4. 字母
            # 累加即可
            else:
                str_bd += ch

        return str_bd
