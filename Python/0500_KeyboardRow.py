class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {
            1: set('qwertyuiop'),
            2: set('asdfghjkl'),
            3: set('zxcvbnm')
        }

        result = []
        for word in words:
            flag = 0
            valid = True
            # 检查每个字母
            for ch in word:
                ch = ch.lower()
                # 遇到第一个字母，flag 为默认状态 0
                if not flag:
                    # 找到该字母属于哪一个 row
                    for key in rows.keys():
                        if ch in rows[key]:
                            flag = key
                # 其余字母，检查是否存在于同一个 row
                else:
                    if ch not in rows[flag]:
                        valid = False
            if valid:
                result.append(word)

        return result
