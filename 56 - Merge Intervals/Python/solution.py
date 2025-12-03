class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key = lambda interval: interval[0])

        last_i = intervals[0]
        
        for interval in intervals[1:]:
            if last_i[1] >= interval[0]:
                end = max(last_i[1], interval[1])
                last_i = [last_i[0], end]
            else:
                ans.append(last_i)
                last_i = interval
        ans.append(last_i)
        return ans

        
