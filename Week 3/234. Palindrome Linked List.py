def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        # go to the end, and find the tail

        tail = head
        arr = []
        while (tail.next != None):
            arr.append(tail.val)
            tail = tail.next

        arr.append(tail.val)

        start = 0
        end = len(arr)-1

        while (start <= end):
            if (arr[start] != arr[end]):
                return False

            start += 1
            end -= 1
        
        
        return True
