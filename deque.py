<<<<<<< HEAD

class Solution(object):
    def mergeLists(self, list1, list2):
        temp1, temp2 = list1, list2
        mergedListHead = ListNode(0) # у указателя нового списка нет значения
        ret = mergedListHead
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    mergedListHead.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    mergedListHead.next = ListNode(temp2.val)
                    temp2 = temp2.next
            elif temp1:
                mergedListHead.next = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp2:
                mergedListHead.next = ListNode(temp2.val)
                temp2 = temp2.next
            mergedListHead = mergedListHead.next

        return ret.next
=======

class Solution(object):
    def mergeLists(self, list1, list2):
        temp1, temp2 = list1, list2
        mergedListHead = ListNode(0) # у указателя нового списка нет значения
        ret = mergedListHead
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    mergedListHead.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    mergedListHead.next = ListNode(temp2.val)
                    temp2 = temp2.next
            elif temp1:
                mergedListHead.next = ListNode(temp1.val)
                temp1 = temp1.next
            elif temp2:
                mergedListHead.next = ListNode(temp2.val)
                temp2 = temp2.next
            mergedListHead = mergedListHead.next

        return ret.next
>>>>>>> 377c49ca12790a6af5e29b52df70fe7fbe5845be
                            