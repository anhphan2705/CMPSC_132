# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        
    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.root == None:
            return True
        else:
            return False

    def _mirrorHelper(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return None
        else:
            new_node = Node(node.value)
            #Recursion through all the branches
            node_left = self._mirrorHelper(node.left)
            node_right = self._mirrorHelper(node.right)
            #Switching branches to the new node
            new_node.left = node_right
            new_node.right = node_left
            return new_node

    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        elif self.root.left == None:
            return self.root
        else:
            temp_root = self.root
            #Go to the left until min
            while temp_root.left is not None:
                temp_root = temp_root.left
            return temp_root

    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        elif self.root.right == None:
            return self.root
        else:
            temp_root = self.root
            #Go to the right until max
            while temp_root.right is not None:
                temp_root = temp_root.right
            return temp_root

    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        
        temp_root = self.root
        temp_root_copy = temp_root
        
        while temp_root != None and temp_root_copy.value != value:
            # Comparing value to find the appropriate branch to go to
            # End when the end of the branch or value match
            if value < temp_root.value:
                temp_root_copy = temp_root
                temp_root = temp_root.left
            elif value > temp_root.value:
                temp_root_copy = temp_root
                temp_root = temp_root.right
            else:
                temp_root_copy = temp_root
            
        if temp_root_copy.value == value:
            return True
        else:
            return False

    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        #Check if empty branch
        if node is None:
            return -1
        #Find the deeper branch
        else:
            return 1 + max(self.getHeight(node.right), self.getHeight(node.left))

if __name__ == '__main__':
    import doctest
    doctest.testmod()