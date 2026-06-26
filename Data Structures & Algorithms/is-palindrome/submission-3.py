class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:

            while (not (s[end].isalnum())) and (start < end):
                end -=1
            while (not (s[start].isalnum())) and (start < end):
                start +=1
            if(s[end].lower() != s[start].lower()):
                return False
            end -=1
            start +=1
        return True
        