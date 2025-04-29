class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # keep a hashmap of the running sum from each side
        
        def isValidPartition(arr):
            leftsums = {}

            i = 0
            runningsum = 0
            while (i < len(arr)):
                runningsum += arr[i]

                if (runningsum in leftsums):
                    leftsums[runningsum].append(i)
                else:
                    leftsums[runningsum] = [i]


                i += 1
            
            # print(leftsums)


            i = len(arr)-1
            runningsum = 0
            while (i >= 0):
                runningsum += arr[i]

                # print("IND", runningsum, i)

                if (runningsum in leftsums and i-1 in leftsums[runningsum]):
                    # print(i, runningsum, leftsums[runningsum])
                    return True
                

                i -= 1

            return False
        
        nums.sort()

        return isValidPartition(nums)
