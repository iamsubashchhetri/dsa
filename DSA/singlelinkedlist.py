class Node:
    def __init__(self, val):
     
        self.val = val
        self.next = None


class SinglyLInkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def append(self, val):
    
        new_node = Node(val)
        if self.head == None:               # Case 1: List is empty
            self.head = new_node
        else:                               # Case 2: Traverse to last node
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node            # Link last node to new node

    def traversal(self):
        """
        Traverse through the list and print all values.
        """
        if self.head is None:               # Empty list check
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")    # Print node value
                curr = curr.next
            print()                         # Newline after traversal

    def insertion(self, val, position):
     
        new_node = Node(val)

        if position == 0:                   # Case 1: Insert at head
            new_node.next = self.head
            self.head = new_node
        else:                               # Case 2: Insert at given position
            current = self.head
            prev_node = None
            count = 0

            # Traverse until reaching desired position
            while current is not None and count < position:
                prev_node = current
                current = current.next      # FIXED (it was current.next = current)
                count += 1

            # Insert node between prev_node and current
            prev_node.next = new_node
            new_node.next = current

    def delete(self, val):
        
        temp = self.head

        # Case 1: List has more than one node, and head needs deletion
        if temp and temp.val == val:
            self.head = temp.next
            return

        # Case 2: Search in the rest of the list
        found = False
        prev = None
        while temp is not None:
            if temp.val == val:             # Node found
                found = True
                break
            prev = temp
            temp = temp.next

        if found:                           # Node found -> unlink it
            prev.next = temp.next
            return
        else:                               # Node not found
            print("Node not found")


# Example Usage:
# sll = SinglyLInkedList()
# sll.append(10)
# sll.append(20)
# sll.append(30)
# sll.traversal()  # Output: 10 20 30
# sll.insertion(15, 1)
# sll.traversal()  # Output: 10 15 20 30
# sll.delete(20)
# sll.traversal()  # Output: 10 15 30
###############################################
# Leetcode 876: Middle of the Linked List
###############################################

# Problem:
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Slow & Fast Pointer
        slow = head
        fast = head

        # Move fast pointer 2 steps and slow pointer 1 step
        # When fast reaches end, slow will be at the middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# Time Complexity: O(n)  
# Space Complexity: O(1)


###############################################
# Leetcode 206: Reverse Linked List
###############################################

# Problem:
# Reverse a singly linked list and return the new head.


# -------------------- Approach 1: Using Stack (Extra Space) --------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []

        # Store values in stack
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        
        # Reassign values in reverse order
        temp = head
        while temp is not None:
            temp.val = stack.pop()
            temp = temp.next
        
        return head

# Time Complexity: O(n)  
# Space Complexity: O(n)


# -------------------- Approach 2: Iterative Optimal Solution --------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None

        # Iteratively reverse pointers
        while temp is not None:
            front = temp.next   # Store next node
            temp.next = prev    # Reverse link
            prev = temp         # Move prev ahead
            temp = front        # Move current ahead

        return prev

# Time Complexity: O(n)  
# Space Complexity: O(1)


###############################################
# Leetcode 141: Linked List Cycle
###############################################

# Problem:
# Given head of a linked list, determine if it has a cycle.
# Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Move fast pointer 2 steps and slow pointer 1 step
        # If they meet, cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

# Time Complexity: O(n)  
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



"""
Leetcode 142 - Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins.
If there's no cycle, return None.

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Step 1: Detect if cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Step 2: Find cycle start
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # cycle start node
        return None  # no cycle

"""
Input:  head = [1 → 2 → 3 → 4 → 5]
         and 5 connects back to 3
Output: 3
Explanation: The cycle is (3 → 4 → 5), so length = 3.

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countNodesinLoop(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head

        while fast  is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow==fast:
                count=1
                temp=slow.next
                while slow!=temp:
                 count+=1
                 temp=temp.next
                return count
        return 0
    


"""
Understand the Problem
You’re given a singly linked list.You need to reorder the nodes so that:All nodes at odd positions come first
Then all nodes at even positions
Example:

Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 3 -> 5 -> 2 -> 4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd=head
        even=head.next
        even_head=even
        while even is not None and even.next is not None:
            odd.next= odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head

        return head

"""
Problem:

Given the head of a singly linked list, remove the nth node from the end of the list and return the modified list.

Follow-up: Can you do it in one pass?

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The 2nd node from the end is 4, which is removed.

"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
             
        if fast==None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next

        return head