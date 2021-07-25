# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        merged_list=[]
        while len(l1)>0 or len(l2)>0:
            if l1==[]:
                merged_list.append(l2.pop(0))
            elif l2==[]:
                merged_list.append(l1.pop(0))
            elif l1[0] < l2[0]:
                merged_list.append(l1.pop(0))
            else:
                merged_list.append(l2.pop(0))
        return merged_list


