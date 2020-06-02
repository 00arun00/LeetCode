class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Args:
            l1: (ListNode) link list of digits
            l2: (ListNode) link list of digits 
        Returns:
            sum_list: (ListNode) link list which has the final sum
        ___________________________________________________________
        Key Concepts:
            - linked lists
        Time Complexity:
            -O(n)
        Space Complexity:
            -O(n)
        """
        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1
        # initialization
        carry = 0
        dummy = curr = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry //= 10

        return dummy.next
