# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> -7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 8.76 -> 9.78 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        node = Node(value)
        # Initializing head and tail if empty
        if self.isEmpty():
            node.next = self.head
            self.head = node
            self.tail = node
        # Assigning the next value for node and head if the head value is larger than node value
        elif self.head.value > node.value:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            while temp.next is not None and temp.next.value < node.value:
                temp = temp.next
            if temp.next is None:
                self.tail = node
            node.next = temp.next
            temp.next = node


    def replicate(self):
        # --- YOUR CODE STARTS HERE
        temp = self.head
        new_link_list = SortedLinkedList()
        while temp is not None:
            if isinstance(temp.value, float) or temp.value < 0:
                new_link_list.add(temp.value)
                new_link_list.add(temp.value)
            elif temp.value == 0:
                new_link_list.add(temp.value)
            else:
                for pos in range(temp.value):
                    new_link_list.add(temp.value)
            temp = temp.next
            
        return new_link_list
                
    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        if self.head != None:
            temp = self.head
            # Removing dupl
            while temp.next is not None:
                if temp.value == temp.next.value:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
                    
if __name__=='__main__':
    import doctest
    doctest.testmod()