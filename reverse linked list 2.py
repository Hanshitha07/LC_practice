
class Solution:
    def reverseBetween(self, head, left, right):

        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before left
        prev = dummy

        for i in range(left - 1):
            prev = prev.next

        # Current node (first node to reverse)
        curr = prev.next

        # Reverse the required portion
        for i in range(right - left):

            next_node = curr.next

            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
