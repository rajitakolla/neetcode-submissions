class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)
        return sCounter == tCounter


# Time complexity : o(N)
# spcae complexity : o(1)  