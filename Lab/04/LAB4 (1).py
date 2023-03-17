# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
#Evan Yuan
# I worked on this asssingment using this semester's course materials and referredd to websites below



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

    def __iter__(self):
        return self
    
    def __next__(self):
        return self

    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value)
        # give the head and tail inital values
        if self.isEmpty():
            new_node.next = self.head 
            self.head = self.tail = new_node
        #if value of head value is greater than the value of the new node, assign the new nodes nexts value as the current head value, and assign the new head value with the value of the new node 
        elif self.head.value > new_node.value:
            new_node.next = self.head
            self.head = new_node
        #traverse list to find right positon for the new node
        else:
            current  = self.head
            while current.next is not None and current.next.value < new_node.value:
                current = current.next
            #when we are at the last node, assign the new node as a tail
            if current.next is None:
                self.tail = new_node
            new_node.next = current.next
            current.next = new_node



    def replicate(self):
        # --- YOUR CODE STARTS HERE
   
        new = SortedLinkedList()
        current  = self.head
        while current != None:
            data = current.value
            #if data is 0, add one zero
            if data == 0:
                new.add(data)
            #if data is float type, add twice
            elif isinstance(data, float):
                new.add(data)
                new.add(data)
            #if data is negative, add twice
            elif data < 0:
                new.add(data)
                new.add(data)
            #use loop to find number of times to add date
            else:
                for i in range(data):
                    new.add(data)
            current =  current.next
        return new
        



    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        
        current  = self.head
        while current != None and current.next != None:
            if current.value == current.next.value:
                current.next = current.next.next
                if current.next == None:
                    self.tail = current
            else:
                current = current.next

if __name__=='__main__':
    import doctest
    doctest.testmod()  
        
       