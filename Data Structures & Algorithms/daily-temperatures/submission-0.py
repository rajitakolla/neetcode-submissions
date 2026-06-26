class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        lenList = len(temperatures)

        result = [0]*len(temperatures)
        tempStack = list()


        for i in range(lenList):
            while tempStack and temperatures[i] > tempStack[-1][0]:
                val,j = tempStack.pop()
                result[j] = (i-j)
            tempStack.append([temperatures[i],i])
        return result