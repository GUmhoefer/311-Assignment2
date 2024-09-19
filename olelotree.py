from olelonode import OleloNode as onode
import string

class OleloTree:
    def __init__(self):
        self.NIL_LEAF = onode(None, None, None, None, 'black')
        self.root = self.NIL_LEAF

        self.olelo_wordlist = {}
        self.english_wordlist = {}

    def _l_rotate(self, x):
        pass

    def _r_rotate(self, y):
        pass

    def insert(self, hphrase, ephrase, hexplain, eexplain):
        hawaiian_words = [word.strip(string.punctuation) for word in hphrase.split()]
        english_words = [word.strip(string.punctuation) for word in ephrase.split()]

        for hword in hawaiian_words:
            if hword not in self.olelo_wordlist:
                self.olelo_wordlist[hword] = []
            self.olelo_wordlist[hword].append((hphrase, ephrase))

        for eword in english_words:
            if eword not in self.english_wordlist:
                self.english_wordlist[eword] = []
            self.english_wordlist[eword].append((hphrase, ephrase))




    def _insert_fixup(self, z):
        pass

    def first(self, x):
        pass
    
    def last(self, x):
        pass

    def successor(self, phrase):
        pass

    def predecessor(self, phrase):
        pass

    def is_member(self, phrase):
        pass

    def mehua(self, word):
        pass

    def withword(self, word):
        pass


