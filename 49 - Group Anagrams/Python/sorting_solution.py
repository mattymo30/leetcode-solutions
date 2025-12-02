class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        store_dict = dict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in store_dict:
                store_dict[sorted_s] = [s]
            else:
                store_dict[sorted_s].append(s)
        
        for v in store_dict:
            ans.append(store_dict[v])
        return ans

