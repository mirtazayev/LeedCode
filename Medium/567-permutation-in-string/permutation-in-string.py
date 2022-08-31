from typing import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = len(s1)
        count = Counter(s1)

        for i in range(len(s2) - s + 1):
            count_2 = Counter(s2[i:i + s])
            if count_2 == count:
                return True
        return False