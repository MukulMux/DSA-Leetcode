#917. Reverse Only Letters
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalpha():
                start += 1
                continue
            if not s[end].isalpha():
                end -= 1
                continue
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)

