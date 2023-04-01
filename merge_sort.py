class Solution:

    def merge(self, nums1, nums2):
        nums = []
        l1 = len(nums1)
        l2 = len(nums2)
        p1,p2,p = 0
        while p1 != l1 and p2 != l2:
            
            if p1 == l1:
                nums[p:] = nums2[p2:]
            elif p2 == l2:
                nums[p:] = nums1[p1:]

            if nums1[p1] <= nums2[p2]:
                nums[p] = nums1[p1]
                p1 += 1
            else:
                nums[p] = nums1[p2]
                p2 += 1
            p += 1
        return nums

    def mergeSort(self, nums):
        if (len(nums) <= 1):
            return nums
        
        m = int(len(nums)/2)
        nums1 = self.mergeSort(nums[:m+1])
        nums2 = self.mergeSort(nums[m+1:])
        
        nums = self.merge(nums1, nums2)
        
        return nums

    def sortArray(self, nums):
        return self.mergeSort(nums)

arr = [1,4,6,7,4,3,4,67,65,34,2,56,54, 3,42,456,7 ,6,3, 53,56,6,667,8, 7,6,54,5,4,6,7,6,534,5,345,6,5,65]
arr = Solution.sortArray(arr)
print(arr)
