class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash Map
        #iterate through the list, sort each element then add to hash map
        #if its in hash map, add to appropriate index (value)
        #if not create its own 

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