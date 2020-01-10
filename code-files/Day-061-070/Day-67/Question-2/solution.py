class Solution:
    tribonacciSequence = {}
    def tribonacci(self, n: int) -> int:
        ht = {}
        for i in range(n+1):
            if i == 0:
                ht[i] = 0
            elif i == 1 or i == 2:
                ht[i] = 1
            else:
                ht[i] = ht[i-1] + ht[i-2] + ht[i-3]
        return ht[n]