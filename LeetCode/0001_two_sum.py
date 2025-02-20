from typing import List

class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        o = []
        for i in range(len(n)-1):
            for j in range(i+1, len(n)):
                if n[i] + n[j] == t:
                    o.append(i)
                    o.append(j)
                    return o