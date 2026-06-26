class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)

        #build a hashmap for t
        for i in t:
            countT[i] += 1

        have, need = 0, len(countT)
        resultLen , result = len(s)+1, [-1,-1]
        start = 0

        for i in range(len(s)):
            ch = s[i]
            window[ch] += 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:

                if (i-start+1) < resultLen:
                    result = [start, i]
                    resultLen = (i-start+1)
                
                window[s[start]] -= 1
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have -= 1
                start +=1

        if resultLen < len(s)+1:
            return s[result[0]:result[1]+1]
        return ""
        pass