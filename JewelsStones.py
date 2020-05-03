class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        l1 = []
        count=0
        for i in J:
            l1.append(i)
        for stone in S:
            if stone in l1:
                count+=1
        return count