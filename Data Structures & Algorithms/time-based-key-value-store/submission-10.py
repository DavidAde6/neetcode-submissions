class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[],[]]
        self.store[key][0].append(value) 
        self.store[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # if key not in Alice, aint doing a thing
        # check if timestamp exists, if not return last element in arr
        if key not in self.store:
            return ""
        timestamps = self.store[key][1]
        l = 0
        r = len(timestamps) -1

        if timestamp < timestamps[0]:
            return ""
        
        result = ""
        while l <= r:
            mid = l + (r - l) // 2
            if timestamps[mid] <= timestamp:
                result = self.store[key][0][mid]
                l = mid + 1
            else:
                r = mid - 1
            


        # if key doesnt exist, the key slightly smaller should be used
        return result
