from olelonode import OleloNode as onode
import string

class OleloTree:

    # Constructor, _l_rotate, _r_rotate coded by Gregor Umhoefer
    def __init__(self):
        self.NIL = onode(None, None, None, None, 'black')
        self.root = self.NIL

    def _l_rotate(self, x):
        y = x.right # Sets y as x's right subtree
        x.right = y.left # Sets y's left subtree as x's right subtree
        if y.left != self.NIL:
            y.left.parent = x # If left subtree is not NIL, sets left subtree's parent to x
        y.parent = x.parent # Sets y's parent to x's parent
        if x.parent == self.NIL: # If x is the root, sets y as the new root
            self.root = y
        elif x == x.parent.left: # If x is a left child, sets y as the new left child
            x.parent.left = y
        else:
            x.parent.right = y # Sets y as the new right child if x was a right child

        # Sets pointers for y's left child and x's parent as x and y respectively
        y.left = x
        x.parent = y

    def _r_rotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    # Insert method coded by Gregor Umhoefer
    def insert(self, hphrase, ephrase, hexplain, eexplain):
        new_node = onode(hphrase, ephrase, hexplain, eexplain)

        # Sets new node's left and right children to NIL
        new_node.left = self.NIL
        new_node.right = self.NIL


        # Sets x to the current node to compare new node to, and y to parent of new node
        x = self.root
        y = self.NIL

        while x != self.NIL:
            # If the tree is not empty, sets the current node as the new parent
            y = x

            # If the new node's phrase is less than the current node's phrase, move left
            # If the new node's phrase is greater than the current node's phrase, move right.
            # Also checks for duplicate phrases.
            if new_node.phrase_olelo < x.phrase_olelo:
                x = x.left
            elif new_node.phrase_olelo > x.phrase_olelo:
                x = x.right
            else:
                print("Duplicate phrase")
                return
        
        # Sets the new node's parent to new parent node after traversing, or to
        # the root if the tree is empty.
        new_node.parent = y

        # Assigns the new node to the correct position relative to the parent
        if y == self.NIL:
            self.root = new_node
        elif new_node.phrase_olelo < y.phrase_olelo:
            y.left = new_node
        else:
            y.right = new_node

    
        self._insert_fixup(new_node)
        
    # _insert_fixup method coded buncle Gregor Umhoefer
    def _insert_fixup(self, node):
        while node.parent != self.NIL and node.parent.color == 'red':
            # If the  node's parent is a left child
            if node.parent == node.parent.parent.left: # If  node's parent and uncle are red
                uncle = node.parent.parent.right  # Sets uncle to the right uncle of  node
                
                # Case 1: If uncle is red, sets parent and uncle to black, and grandparent to red
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent # Sets node to grandparent continue to check red black conflicts
                else:
                    # Case 2: If uncle is black and node is a right child
                    # Sets node to parent and rotates left
                    if node == node.parent.right:
                        node = node.parent
                        self._l_rotate(node)

                    # Sets parent to black and grandparent to red, then rotates right
                    node.parent.color = 'black' 
                    node.parent.parent.color = 'red'
                    self._r_rotate(node.parent.parent)
            else: # If the new node's parent is a right child
                uncle = node.parent.parent.left # Sets uncle to the left uncle of new node

                # Case 3: If uncle is red, sets parent and uncle to black, and grandparent to red
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:

                    # Case 4: If uncle is black and node is a left child
                    # Sets node to parent and rotates right
                    if node == node.parent.left:
                        node = node.parent
                        self._r_rotate(node)

                    # Sets parent to black and grandparent to red, then rotates left
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._l_rotate(node.parent.parent)
        self.root.color = 'black'

    # First and lasts methods coded by Gregor Umhoefer
    def first(self, x):

        # Continuously moves left to find the leftmost node
        while x.left != self.NIL:
            x = x.left
        return x
    
    def last(self, x):

        # Continuously moves right to find the rightmost node
        while x.right != self.NIL:
            x = x.right
        return x

    # Successor method coded by Brendan Kuwabara
    def successor(self, phrase):
        # Step 1: Search for the node with the matching phrase
        current = self.root

        while current != self.NIL:
            if phrase < current.phrase_olelo: 
                current = current.left
            elif phrase > current.phrase_olelo:
                current = current.right
            else:
                break  # Found the node

        if current == self.NIL:
            return "Phrase not found" # Phrase not found in the tree

        # Step 2: If the node has a right child, find the minimum in the right subtree
        if current.right != self.NIL:
            current = current.right # Setting the current to the right node to search the right subtree
            while current.left != self.NIL: # accessing the minimum value in the right subtree
                current = current.left
            return current
        
        # Step 3: If there is no right child, find the lowest ancestor for which the node is in the left subtree
        parent = current.parent
        while parent != self.NIL and current == parent.right:
            current = parent
            parent = parent.parent
        
        if parent == self.NIL:
            return "No successor"
        else:
            return parent

    # predecessor method coded by Brendan Kuwabara
    def predecessor(self, phrase):
        # Step 1: Search for the node with the matching phrase
        current = self.root
        while current != self.NIL:
            if phrase < current.phrase_olelo:  
                current = current.left
            elif phrase > current.phrase_olelo:
                current = current.right
            else:
                break  # Found the node

        if current == self.NIL:
            return "Phrase not found" # Phrase not found in the tree

        # Step 2: If the node has a left child, find the maximum in the left subtree
        if current.left != self.NIL:
            current = current.left
            while current.right != self.NIL:
                current = current.right
            return current

        
        # Step 3: If no left child, find the lowest ancestor for which the node is in the right subtree
        parent = current.parent
        while parent != self.NIL and current == parent.left:
            current = parent
            parent = parent.parent
        
        if parent == self.NIL:
            return "No predecessor"
        else:
            return parent

    # is_member is a function that takes a node and a phrase, then searches the red and black tree to see if the phrase is present
    # If the phrase is present, the function returns true, if the phrase is not present, it will return false
    # is_member method coded by Brendan Kuwabara
    def is_member(self, phrase):
        current = self.root
        # Search the tree for the phrase passed into the function
        while current != self.NIL:
            if phrase < current.phrase_olelo: # If input phrase is smaller, go to the left
                current = current.left
            
            elif phrase > current.phrase_olelo: # If input phrase is bigger, go to the right 
                current = current.right
            
            else:
                return True #If the phrase matches the current node, return true because the node is a member
        
        return False # If a node is not found with the phrase, then it is not a member of the tree


    # Mehua method coded by Brendan Kuwabara
    def MeHua(self, word):

        result = []
        stack = []  # Stack for tree traversal
        current = self.root

        # Traverse the tree in order
        while stack or current != self.NIL:
            if current != self.NIL:
                stack.append(current)
                current = current.left  # Move to the left child
            else:
                current = stack.pop()
                
                # Check if the word exists in the current node's olelo_wordlist
                if current.olelo_search(word):
                    result.append(current.phrase_olelo)

                current = current.right  # Move to the right child

        return result


    # WithWord method coded by Brendan Kuwabara
    def WithWord(self, word):
       
        result = []
        stack = []  # Stack for iterative tree traversal
        current = self.root

        # Iterative in-order traversal
        while stack or current != self.NIL:
            if current != self.NIL:
                stack.append(current)
                current = current.left  # Move to the left child
            else:
                current = stack.pop()
                
                # Check if the word exists in the current node's english_wordlist
                if current.english_search(word):
                    result.append(current.phrase_english)

                current = current.right  # Move to the right child

        return result
    

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        stack = []
        if node != self.NIL:
            self._in_order(node.left)
            print(node.phrase_olelo)
            self._in_order(node.right)


