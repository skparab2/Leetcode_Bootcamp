class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 0):
            return 0

        wholesum = sum(nums)

        if (len(nums) == 1):
            return wholesum

        leftsums = {}

        i = 0
        runningsum = 0
        while (i < len(nums)):
            runningsum += nums[i]

            leftsums[i] = runningsum
            i += 1

        
        # print(leftsums)




        rightsums = {}

        i = len(nums) - 1
        runningsum = 0
        while (i >= 0):
            runningsum += nums[i]

            rightsums[i] = runningsum

            i -= 1

        
        # print(rightsums)

        # print(wholesum)


        maxsum = wholesum

        front = 0
        back = 1
        while (True):
            
            # print("front", front, "back", back)

            if (front == 0 and back == len(nums)):
                thissum = wholesum
            elif (front == 0):
                thissum = wholesum - rightsums[back]
            elif (back == len(nums)):
                thissum = wholesum - leftsums[front] + nums[front]
            else:
                thissum = wholesum - leftsums[front] + nums[front] - rightsums[back]

            # print(thissum)

            maxsum = max(maxsum, thissum)
    

            if (front >= len(nums)-1 and back >= len(nums)):
                break
            elif (back == len(nums)):
                front += 1
                back = front+1
            else:
                back += 1

        return maxsum
