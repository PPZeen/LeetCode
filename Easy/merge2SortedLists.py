class Solution:
    def mergeTwoLists(self, list1, list2):
        #n = ListNode()
        a = n
        while list1 != None or list2 != None:
            if list1 == None:
                n.next = list2
                break
            elif list2 == None:
                n.next = list1
                break
            else:
                if list1.val <= list2.val:
                    n.next = list1
                    list1 = list1.next
                else:
                    n.next = list2
                    list2 = list2.next
                n = n.next
        return a.next