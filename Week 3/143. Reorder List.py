def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # put all the nodes in an arr
        arr = []
        nd = head
        while (nd.next != None):
            arr.append(nd)
            nd = nd.next

        arr.append(nd)

        start = 0
        end = len(arr)-1

        while (start < end):
            arr[start].next = arr[end]

            # print("arr[start] is",arr[start].val,"now has a next of", arr[start].next.val)

            start += 1

            if (start >= end):
                break

            arr[end].next = arr[start]

            # print("arr[end] is",arr[end].val,"now has a next of", arr[end].next.val)

            end -= 1

            # print(start, end)

        arr[start].next = None
