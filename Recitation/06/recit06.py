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
        if self.root is None:
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
        
    def numChildren(self, node_object):
        
        number = 0
        if node_object.left is not None:
            number +=1
        if node_object.right is not None:
            number += 1
            
        return number
    
    def __delitem__(self, value):
        self._deleteHelper(None, self.root, value)
        return self.printInorder
    
 

    def __delitem__(self, value):
        self._deleteHelper(None, self.root, value)
        return self.printInorder
    

    def _deleteHelper(self, parent, current, value):
        if current is None:
            return None 
        if current.value>value:
            self._deleteHelper(current, current.left, value) #[1]
        elif current.value<value:
            self._deleteHelper(current, current.right, value) #[2]
        else:

            node_children=self.numChildren(current)

            if node_children==0 or node_children==1:

                if current.left is not None:
                    child = current.left #[3]
                else:
                    child = current.right #[4]

                if (parent is not None) and (parent.left is current):
                    parent.left = child #[5]
                elif (parent is not None) and (parent.right is current):
                    parent.right = child #[6]
                else:
                    self.root = child #[7]
            else:

                temp = current.right
                parent = current
                while temp.left is not None: 
                    parent = temp #[8]
                    temp = temp.left #[9]

                current.value= temp.value #[10]
                self._deleteHelper(parent, temp, temp.value) #[11]
    

    
bst_keys = [3, 2, 5, 4, 9, 3.5, 6]
t = BinarySearchTree()
for key in bst_keys:
    t.insert(key)

print(t.numChildren(t.root))              # Displays 2
print(t.numChildren(t.root.left))         # Displays 0
print(t.numChildren(t.root.right))        # Displays 2
print(t.numChildren(t.root.right.right))  # Displays 1