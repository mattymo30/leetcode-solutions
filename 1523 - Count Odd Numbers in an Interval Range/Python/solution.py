class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low + 1

        if diff % 2 == 1:
            return ((high + 1) // 2) - (low // 2)
        else:
            return (diff // 2)
            
        
