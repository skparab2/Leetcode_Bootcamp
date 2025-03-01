class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # check if it is already sorted
        srt = True
        j = 1
        while (j < len(nums)):
            if (nums[j-1] > nums[j]):
                srt = False
                break
            j += 1

        if (srt):
            return

        # start at the start and end.
        # swap if they need to be changed.

        # actually do this in two steps
        # first, all the zeros to the left side

        leftpointer = 0
        rightpointer = len(nums) - 1

        streak = 0

        while (leftpointer < rightpointer):
            if (nums[leftpointer] != 0):
                # need to swap
                nums[leftpointer], nums[rightpointer] = nums[rightpointer], nums[leftpointer]

            if (nums[leftpointer] != 0 and nums[rightpointer] == 0):
                streak += 1

            if (streak > 2):
                break

            if (nums[leftpointer] == 0):
                streak = 0
                leftpointer += 1
            
            if (nums[rightpointer] != 0):
                streak = 0
                rightpointer -= 1
            
        
            print(nums)
            print(leftpointer)
            print(rightpointer)
            

        print("moving on")
        # now do the same thing for 1s and 2s
        #leftpointer = 0 can stay what it was

        if (nums[leftpointer] == 0):
            leftpointer += 1
        rightpointer = len(nums) - 1 
        streak = 0

        while (leftpointer < rightpointer):
            if (nums[leftpointer] == 2):
                # need to swap
                nums[leftpointer], nums[rightpointer] = nums[rightpointer], nums[leftpointer]

            if (nums[leftpointer] != 1 and nums[rightpointer] != 2):
                streak += 1

            if (streak > 2):
                break

            if (nums[leftpointer] == 1):
                streak = 0
                leftpointer += 1
            
            if (nums[rightpointer] == 2):
                streak = 0
                rightpointer -= 1
            
        
            print(nums)
            print(leftpointer)
            print(rightpointer)
            
            
        
