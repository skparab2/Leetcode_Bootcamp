class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # do it using two pointers
        leftpointer = 0
        rightpointer = len(numbers)-1

        found = False

        while (not found):
            currentsum = numbers[leftpointer] + numbers[rightpointer]
            
            if (currentsum == target):
                found = True
            elif (currentsum > target):
                rightpointer -= 1
            else:
                leftpointer += 1

        
        return [leftpointer+1, rightpointer+1]
