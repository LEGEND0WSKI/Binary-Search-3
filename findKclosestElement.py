# Time:O(n-k)
# Space:O(1)
# Leetcode:Yes
# Issues:No
#sliding window
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        h = n-1

        while l < h:
            disA = abs(arr[l]-x)
            disB = abs(arr[h]-x)

            if disA <= disB:
                h-=1
            else:
                l+=1

        return arr[l:l+k]
    
# Time: O(log(n-k)+k)
# Space:O(1)
# Leetcode: Yes
# Issues:No
#binary search
class Solution2: 
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        low = 0
        high = n-k

        while low < high:
            mid = low + (high-low)//2

            disS = x - arr[mid]
            disE = arr[mid+k] - x
            
            if disS > disE:
                low = mid +1
            else:
                high = mid

        return arr[low:low+k]