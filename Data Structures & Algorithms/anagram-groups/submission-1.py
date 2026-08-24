class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        result = []
        for i, n in enumerate(strs):
            sort = ''.join(sorted(n))
            if sort in hmap:
                hmap[sort].append(n)
            else:
                hmap[sort] = [n]
        for i in hmap:
            result.append(hmap[i])
        return result