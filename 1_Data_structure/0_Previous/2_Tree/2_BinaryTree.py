'''
reference
http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html

Binary tree
+ it use for search or sorting efficiently
+ time complexity(when search): O(log n) -> I know that because use recursion
    + while use heap: O(nlog n) -> why? 

+ Conditions  
    + left child is smallest or equal than current node
    + right child is biggest or equal than current node
'''

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    # insert method
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else: 
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else: 
                node.right = self._insert_value(node.right, data)
        return node
    
    # search method
    def find(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else: 
            return self._find_value(root.right, key)
        
    # delete method
    '''
    when delete one of child, assume subtree A and B, if biggest than all component of A and smallest than B of others component
    that getting from grand child of left of B 
    
    delete method에 대해 조금 더 알아보기
    '''
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted
    
    def _delete_value(self, node, key):
        if node is None:
            return node, False
        
        deleted = False
        if key == node.data:
            deleted = True
            
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None: 
                    parent, child = child, child.left
                
                child.left = node.left
                
                if parent != node: 
                    parent.left = child.right
                    child.right = node.right
                
                node=child
            
            elif node.left or node.right:
                node = node.left or node.right
            
            else: 
                node=None
        
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        
        else: 
            node.right, deleted = self._delete_value(node.right, key)
            
        return node, deleted
            
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BST()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False