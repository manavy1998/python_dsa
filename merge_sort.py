class Solution:

    def merge(self, nums1, nums2):
        nums = []
        l1 = len(nums1)
        l2 = len(nums2)
        p1,p2,p = 0,0,0
        while p1 != l1 and p2 != l2:
            
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1]) 
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
            p += 1
        
        if p1 == l1:
                nums = nums+nums2[p2:]
        elif p2 == l2:
                nums = nums+nums1[p1:]
        return nums

    def mergeSort(self, nums):
        
        if (len(nums) <= 1):
            return nums
        
        m = int(len(nums)/2)
        nums1 = self.mergeSort(nums[:m])
        nums2 = self.mergeSort(nums[m:])
        
        
        nums = self.merge(nums1, nums2)
        print(nums)
        return nums

    def sortArray(self, nums):
        return self.mergeSort(nums)

arr = [1,4,6,7,4,3,4,67,65,34,2,56,54, 3,42,456,7 ,6,3, 53,56,6,667,8, 7,6,54,5,4,6,7,6,534,5,345,6,5,65]
a = Solution()
arr = a.sortArray(arr)
print(arr, end=' len = ' + str(len(arr)))
