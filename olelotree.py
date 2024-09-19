from olelonode import OleloNode as onode
import string

class OleloTree:
    def __init__(self):
        self.NIL = onode(None, None, None, None, 'black')
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
        
        while z.parent.color == 'red':
            # If the new node's parent is a left child
            if z.parent == z.parent.parent.left: # If new node's parent and uncle are red
                y = z.parent.parent.right  # Sets y to the right uncle of new node
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

    def first(self, x):
        while x.left != self.NIL:
            x = x.left
        return x
    
    def last(self, x):
        while x.right != self.NIL:
            x = x.right
        return x

    def successor(self, phrase):
        # Step 1: Search for the node with the matching phrase
        current = self
        while current is not None:
            if phrase < ' '.join(current.phrase_olelo): 
                current = current.left
            elif phrase > ' '.join(current.phrase_olelo):
                current = current.right
            else:
                break  # Found the node

        if current is None:
            return None  # Phrase not found in the tree

        # Step 2: If the node has a right child, find the minimum in the right subtree
        if current.right is not None:
            current = current.right
            
            while current.left is not None:
                current = current.left
            return current
        
        # Step 3: If no right child, find the lowest ancestor for which the node is in the left subtree
        parent = current.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent
        
        return parent
        
        

    def predecessor(self, phrase):
        pass

    def is_member(self, phrase):
        pass

    def mehua(self, word):
        pass

    def withword(self, word):
        pass

    def in_order(self):
        pass


