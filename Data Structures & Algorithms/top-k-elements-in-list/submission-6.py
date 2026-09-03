class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            if n in count:
                count[n] = count[n] + 1
            else:
                count[n] = 1
        for n, c in count.items():
            arr[c].append(n)

        #print(arr)
        for i in range(len(arr)-1, 0, -1):
            for j in arr[i]:
                result.append(j)
                if len(result) >= k:
                    return result


        