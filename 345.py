#345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1
        matching = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while start < end:

            if s[start] not in matching:
                start = start + 1
                continue
            if s[end] not in matching:
                end = end - 1
                continue

            s[start], s[end] = s[end], s[start]
            start = start + 1
            end = end - 1

        return "".join(s)


