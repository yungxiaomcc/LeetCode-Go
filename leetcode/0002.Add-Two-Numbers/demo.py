

from tkinter.messagebox import NO


class Node:
    def __init__(self,value:int) -> None:
        self._value =value
        self._next=None

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,val):
        self._value=val
    
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self,next):
        self._next=next

class LinkedList:

    def __init__(self):
        self._head=None
    
    def is_empty(self):
        return self._head is None
    def add(self,value):
        n = Node(value)
        
        
        
    
    def delete():
        ...

    def size():
        ...


def add_tow_numbers():
    pass

