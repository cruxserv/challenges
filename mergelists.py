list1 = [1, 2, 4]
list2 = [1, 3, 4]
output = sorted(list1 + list2)
print(output)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = [ListNode]
        Dummy.next = min(list1[0], list2[0])
        for i in fl:
            fl[i].next = f[i+1]
        if not list1 or list2:
            return []
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            return Dummy.next


mergeTwoLists([1, 2, 4], [1, 3, 4])
