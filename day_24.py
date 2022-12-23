"""
More Linked Lists

Task
A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance
pointer, next, pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor, which takes a pointer to the head node of a linked list as
a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of
the updated list.

Note: The head pointer may be null, indicating that the list is empty. Be sure to reset your next pointer when
performing deletions to avoid breaking the list.

Input Format
You do not need to read any input from stdin. The following input is handled by the locked stub code and passed to the removeDuplicates function:
The first line contains an integer, N, the number of nodes to be inserted.
The N subsequent lines each contain an integer describing the data value of a node being inserted at the list's tail.

[1, 2, 2, 3, 3, 4] -> [1, 2, 3, 4]
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if not head:
            return head
        current = head
        while current:
            while current.next is not None and current.data == current.next.data:
                current.next = current.next.next
            current = current.next
        return head



mylist = Solution()
head = None
input_list = [1, 1, 1, 1, 1, 1, 1]
for data in input_list:
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
print("\nExpected output: 1")


