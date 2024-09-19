"""
OleloNode Class
Author: Gregor Umhoefer
Date: 9/17/2024
Description: This class stores the phrases, translations, and descriptions for
             a node used in the red black tree database. It also stores pointers
             to the node's left and right children, as well as its parent.
             It also has a color attribute for red black tree implementation.
"""
import string

class OleloNode:
    def __init__(self, phrase_olelo, phrase_english, exp_olelo, exp_english, color = 'red'):

        if (phrase_olelo != "NIL" and phrase_english != "NIL"):
            self.phrase_olelo = phrase_olelo.split()
            self.phrase_english = phrase_english.split()
            self.olelo_wordlist = [word.strip(string.punctuation) for word in phrase_olelo.split()]
            self.english_wordlist = [word.strip(string.punctuation) for word in phrase_english.split()]
        else:
            self.phrase_olelo = phrase_olelo
            self.phrase_english = phrase_english
        self.exp_olelo = exp_olelo
        self.exp_english = exp_english

        self.left = None  # Left child node
        self.right = None  # Right child node
        self.parent = None # Pointer to parent node

        self.color = color # Color for red black tree

    def __str__(self):
        return f"Phrase in Olelo Hawaiʻi:\n{' '.join(self.phrase_olelo)}\n"
        f"\n\nPhrase in English:\n{' '.join(self.phrase_english)}\n"
        f"\n\nExplanation in Olelo Hawaiʻi:\n{self.exp_olelo}\n"
        f"\n\nExplanation in English:\n{self.exp_english}\n"