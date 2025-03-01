class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        endarr = []
        i = 0
        while (i < len(nums)):
            endarr.append(1)
            i += 1

  
        # start at the start

        i = 0
        currentproduct = 1
        while (i < len(nums)):
            endarr[i] = currentproduct
            currentproduct *= nums[i]
            i += 1

        i -= 1

        currentproduct = 1
        while (i >= 0):
            endarr[i] *= currentproduct
            currentproduct *= nums[i]
            i -= 1
        
        return endarr
