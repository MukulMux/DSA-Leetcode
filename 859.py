#859. Buddy Strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)  # if repeating character then swap possible to make same string

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[
                    i]))  # keeping pairs of mismatches on same index in a list to make sure only one max mismatch is there else it will fail

        if len(diff) != 2:  # need exactly 2 mismatches to swap and make same word again
            return False

        first = diff[0]
        second = diff[1]
        #    return first[0]==second[1] and first[1]==second[0]
        if first[0] == second[1] and first[1] == second[0]:
            return True
        else:
            return False





