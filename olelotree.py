from olelonode import OleloNode as onode
import string

class OleloTree:
    def __init__(self):
        self.NIL = onode("NIL", "NIL", "NIL", "NIL", 'black')
        self.root = self.NIL

        # We may not need these, I'm going to try to implement a sorted list in each node
        # so we can do a binary search on that list when searching for phrases based on a
        # word in the phrase.
        self.olelo_wordlist = {}
        self.english_wordlist = {}

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
        # Splits the words words in the each phrase and removes punctuation
        # hawaiian_words = [word.strip(string.punctuation) for word in hphrase.split()]
        # english_words = [word.strip(string.punctuation) for word in ephrase.split()]

        # # Adds the words to a the word list dictionaries, with the values as
        # # in the dictionary being the phrases that contain that word for rapid lookup.
        # # This is done for both the Hawaiian and English phrases.
        # for hword in hawaiian_words:
        #     if hword not in self.olelo_wordlist:
        #         self.olelo_wordlist[hword] = []
        #     self.olelo_wordlist[hword].append((hphrase, ephrase))

        # for eword in english_words:
        #     if eword not in self.english_wordlist:
        #         self.english_wordlist[eword] = []
        #     self.english_wordlist[eword].append((hphrase, ephrase))

        # Creates a new node with phrases and explanations
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
        

    def _insert_fixup(self, z):
        #print(f"z: {z.phrase_olelo}, z.parent: {z.parent.phrase_olelo}, z.parent.parent: {z.parent.parent.phrase_olelo}")
        while z.parent != self.NIL and z.parent.color == 'red':
            # If the new node's parent is a left child
            if z.parent == z.parent.parent.left: # If new node's parent and uncle are red
                y = z.parent.parent.right  # Sets y to the right uncle of new node\
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent # Sets new node to grandparent continue to check red black conflicts
                else:
                    if z == z.parent.right: # If new node is right child
                        z = z.parent
                        self._l_rotate(z)
                    z.parent.color = 'black' 
                    z.parent.parent.color = 'red'
                    self._r_rotate(z.parent.parent)
            else: # If the new node's parent is a right child
                y = z.parent.parent.left
                print(f"left uncle y is null?")
                print(y)
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._r_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._l_rotate(z.parent.parent)
        self.root.color = 'black'

    def first(self, x):
        while x.left != self.NIL:
            x = x.left
        return x
    
    def last(self, x):
        while x.right != self.NIL:
            x = x.right
        return x

    # Successor method coded by Brendan Kuwabara
    def successor(self, phrase):
        # Step 1: Search for the node with the matching phrase
        current = self
        while current is not None:
            if phrase < ' '.join(current.phrase): 
                current = current.left
            elif phrase > ' '.join(current.phrase):
                current = current.right
            else:
                break  # Found the node

        if current is None:
            return None  # Phrase not found in the tree

        # Step 2: If the node has a right child, find the minimum in the right subtree
        if current.right is not None:
            current = current.right # Setting the current to the right node to search the right subtree
            
            while current.left is not None: # accessing the minimum value in the right subtree
                current = current.left
            return current
        
        # Step 3: If there is no right child, find the lowest ancestor for which the node is in the left subtree
        parent = current.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent
        
        return parent

    # predecessor method coded by Brendan Kuwabara
    def predecessor(self, phrase):
        # Step 1: Search for the node with the matching phrase
        current = self
        while current is not None:
            if phrase < ' '.join(current.phrase):  
                current = current.left
            elif phrase > ' '.join(current.phrase):
                current = current.right
            else:
                break  # Found the node

        if current is None:
            return None  # Phrase not found in the tree

        # Step 2: If the node has a left child, find the maximum in the left subtree
        if current.left is not None:
            current = current.left
            while current.right is not None:
                current = current.right
            return current

        
        # Step 3: If no left child, find the lowest ancestor for which the node is in the right subtree
        parent = current.parent
        while parent is not None and current == parent.left:
            current = parent
            parent = parent.parent
        
        return parent

    # is_member is a function that takes a node and a phrase, then searches the red and black tree to see if the phrase is present
    # If the phrase is present, the function returns true, if the phrase is not present, it will return false
    # is_member method coded by Brendan Kuwabara
    def is_member(self, phrase):

        # Start at current node 
        current = self

        # Search the tree for the phrase passed into the function
        while current is not None:
            if phrase < ' '.join(current.phrase): # If input phrase is smaller, go to the left
                current = current.left
            
            elif phrase > ' '.join(current.phrase): # If input phrase is bigger, go to the right 
                current = current.right
            
            else:
                return True #If the phrase matches the current node, return true because the node is a member
        
        return False # If a node is not found with the phrase, then it is not a member of the tree

    def mehua(self, word):
        pass

    def withword(self, word):
        pass

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node != self.NIL:
            self._in_order(node.left)
            print(node.olelo_wordlist)
            print(node.english_wordlist)
            self._in_order(node.right)


