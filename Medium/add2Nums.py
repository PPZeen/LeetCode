class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    
class LinkList:
    def __init__(self, items=None):
        if items == None or items == ['']:
            self.head = None
        else:
            p = ListNode(items[0])
            self.head = p
            for data in items[1::]:
                q = ListNode(data)
                p.next = p = q
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if self.size(l1) < self.size(l2): l1,l2 = l2,l1 
        ans = []
        while l1 != None:
            x = l1.val + l2.val
            ans.append(ListNode(x%10))
            if x > 9:
                if l1.next == None:
                    ans.append(ListNode(x%10))
                    break
                else:
                    l1.next.val = l1.next.val + 1
                    
            l1 = l1.next
            l2 = l2.next if l2.next != None else ListNode(0)

        for i in range(len(ans)-1): ans[i].next = ans[i+1]
        return ans[0]
    
    def size(self, l):
        count = 0
        t = l
        while t != None:
            count += 1
            t = t.next
        return count
    
l1 = LinkList([9,9,9,9,9,9,9])
l2 = LinkList([9,9,9,9])
ans = Solution().addTwoNumbers(l1.head, l2.head)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         if self.size(l1) < self.size(l2): l1,l2 = l2,l1 
#         ans = []
#         while l1 != None:
#             x = l1.val + l2.val
#             ans.append(ListNode(x%10))
#             if x > 9:
#                 if l1.next == None:
#                     ans.append(ListNode(1))
#                     break
#                 else: l1.next.val = l1.next.val + 1
                    
#             l1 = l1.next
#             l2 = l2.next if l2.next != None else ListNode(0)

#         for i in range(len(ans)-1): ans[i].next = ans[i+1]
#         return ans[0]
    
#     def size(self, l):
#         count = 0
#         t = l
#         while t != None:
#             count += 1
#             t = t.next
#         return count