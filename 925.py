#925. Long Pressed Name
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        lenTyped = len(typed)
        lenName = len(name)
        while j < lenTyped:
            if i < lenName and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == lenName


