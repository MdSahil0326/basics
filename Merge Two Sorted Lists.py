class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to form the new sorted list
        dummy = ListNode()
        tail = dummy
        
        # While both lists are non-empty, compare the values and add the smaller one to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If one list is not empty, add the remaining elements
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # Return the head of the merged list, which is the next node of the dummy
        return dummy.next
