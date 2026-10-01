class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr1 = list(s.lower())
        arr = []
        for i, x in enumerate(arr1):
            if x.isalpha() or x.isdigit():
                arr.append(x)

            
        for i, char in enumerate(arr):
            if char != arr[-(i + 1)]:
                print(char, arr[-(i)])
                return False
            if i == len(arr) - i or i == len(arr) - (i +1) or i == len(arr) - (i -1):
                return True

        return True