"""
Write an iterator for a doubly linked list
"""

class ListNode:
    def __init__(self,val:int,prev:"ListNode"=None,next:"ListNode"=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode :{self.val}"

class LinkedList:
    def __init__(self) -> None:
        self.head,self.tail = self.build_list()

    def build_list(self) -> tuple:
        head,tail = ListNode(0),ListNode(0)
        head.next = tail
        tail.prev = head
        return head,tail
    
    def add(self,val):
        new_node = ListNode(val)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def __iter__(self):
        self.it = self.head.next
        return self
    
    def __next__(self):
        if self.it and self.it.next:
            return_val = self.it
            self.it = self.it.next
            return return_val
        else:
            raise StopIteration
        
import random
if __name__ == '__main__':
    # driver code
    list = LinkedList()
    for _ in range(10):
        list.add(int(10*random.random()))
    
    for node in list:
        print(node)
        