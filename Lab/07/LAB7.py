# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
from ast import List


class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # YOUR CODE STARTS HERE
        if len(self._heap) == 0:
            return None
        else:
            return self._heap[0]
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        if index == 1:
            return None
        else:
            return self._heap[(index//2) - 1]

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        value = index * 2 - 1
        if len(self._heap) <= value:
            return None
        else:
            return self._heap
        
    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        value = index * 2 + 1
        if len(self._heap) <= value:
            return None
        else:
            return self._heap[value]


    def insert(self,item):
        # YOUR CODE STARTS HERE
        self._heap.append(item)
        if len(self._heap) == 1:
            return None
        else:
            len_heap = len(self._heap)
            while self._parent(len_heap) > item:
                parent = self._parent(len_heap)  
                # Find the location              
                index_rplc = len_heap //2 -1
                index_target = len_heap -1
                # Swapping position
                self._heap[index_rplc] = item
                self._heap[index_target] = parent
                len_heap = len_heap //2
                #Check if parent exist
                if self._parent(len_heap) is None:
                    return None
            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            # YOUR CODE STARTS HERE
            deleted = self._heap[self.__len__() -1]
            minValue = self._heap[0]
            self._heap[0] = deleted
            self._heap = self._heap[:1]
            # Relocate items
            pos_heap = 1
            pos = 0 
            while self._rightChild(pos) is not None and self._leftChild(pos) is not None and self._rightChild(pos) <= minValue and self._leftChild(pos) <= minValue:
                right = self._rightChild(pos_heap)
                left = self._leftChild(pos_heap)
                # Move items to the right
                if right < left:
                    self._heap[pos] = right
                    pos = pos *2 +2
                    pos_heap = pos_heap *2 +1
                    self._heap[pos] = deleted
                # Move items to the left
                else:
                    self._heap[pos] = left
                    pos = pos *2 +1
                    pos_heap = pos_heap *2
                    self._heap[pos] = deleted
            # Check the last item
            if self._leftChild(pos_heap) != None and self._leftChild() < deleted:
                self._heap[pos] = self._leftChild(pos_heap)
                pos = pos *2 +1
                self._heap[pos] = deleted
                
            return minValue
                        
def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    # YOUR CODE STARTS HERE
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()