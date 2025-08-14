#1576. Replace All ?'s to Avoid Consecutive Repeating Characters

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':

                if i > 0:
                    left = s[i - 1]
                else:
                    left = ''

                if i < n - 1:
                    right = s[i + 1]
                else:
                    right = ''

                for ch in "abc":
                    if ch != left and ch != right:
                        s[i] = ch
                        break

        return "".join(s)
