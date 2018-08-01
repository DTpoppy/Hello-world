class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math
        for i in range(min(piles),max(piles)+1):
            t = list(map(lambda x: math.ceil(x/i),piles))
            if sum(t) <= H:
                return i
       

str1 = input()
str2 = str1[1:-1:1]
pilex2 = str2.split(',')
pilex = list(map(int,pilex2))
H = int(input())
B = Solution()
print(B.minEatingSpeed(pilex,H))