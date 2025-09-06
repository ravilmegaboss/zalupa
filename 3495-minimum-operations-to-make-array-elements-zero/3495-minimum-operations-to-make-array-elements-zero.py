class Solution:
    def get(self, num):
        i = 1
        j = 1
        c = 0
        while j <= num:
            c += ((i + 1) // 2) * (min(j * 2 - 1, num) - j + 1)
            i += 1
            j *= 2
        return c
    def minOperations(self, queries):
        result = 0
        for q in queries:
            result += (self.get(q[1]) - self.get(q[0] - 1) + 1) // 2
        return result