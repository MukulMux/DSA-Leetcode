#151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        newList = s.split() #splits a string and assigns to newList which is a list

        k = ""
        for i in newList[::-1]:
            k += i.strip() + " "

        return k.strip()
