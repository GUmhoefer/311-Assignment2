"""
OleloNode Class
Author: Gregor Umhoefer
Date: 9/17/2024
Description: This class stores the phrases, translations, and descriptions for
             a node used in the red black tree database. It also stores pointers
             to the node's left and right children, as well as its parent.
             It also has a color attribute for red black tree implementation.

             The class has also stores a list of words from the phrases in both 
             ʻOlelo Hawaiʻi and English. It has methods that implement merge sort to 
             sort the word lists alphabetically, and a binary search method to efficiently
             search these lists for a specific word.
"""
import string

class OleloNode:
    def __init__(self, phrase_olelo, phrase_english, exp_olelo, exp_english, color = 'red'):

        if (phrase_olelo != None and phrase_english != None):
            self.olelo_wordlist = [word.strip(string.punctuation).lower() for word in phrase_olelo.split()]
            self.english_wordlist = [word.strip(string.punctuation).lower() for word in phrase_english.split()]
            self.olelo_wordlist = self.sort_words(self.olelo_wordlist, 0, (len(self.olelo_wordlist) - 1))
            self.english_wordlist = self.sort_words(self.english_wordlist, 0, (len(self.english_wordlist) - 1))
        # else:
        self.phrase_olelo = phrase_olelo
        self.phrase_english = phrase_english
        self.exp_olelo = exp_olelo
        self.exp_english = exp_english

        self.left = None  # Left child node
        self.right = None  # Right child node
        self.parent = None # Pointer to parent node

        self.color = color # Color for red black tree

    def __str__(self):
        return (f"\nPhrase in Olelo Hawaiʻi:\n{self.phrase_olelo}\n"
        f"\nPhrase in English:\n{self.phrase_english}\n"
        f"\nExplanation in Olelo Hawaiʻi:\n{self.exp_olelo}\n"
        f"\nExplanation in English:\n{self.exp_english}\n")


    # Uses merge sort to sort words alphabetically
    def sort_words(self, words, begin, end):
        if begin >= end:
            # Base case if the list has 1 or fewer elements
            return words
        mid = (begin + end) // 2 # Finds the middle of the list, rounded down
        self.sort_words(words, begin, mid) # Recursively splits the left list
        self.sort_words(words, mid + 1, end) # Recursively splits the right list

        # Merges the left and right list for each recursion
        return self.merge(words, begin, mid, end)

    def merge(self, words, begin, mid, end):

        # Sets the number of elements in the left and right lists
        num_left = mid - begin + 1
        num_right = end - mid

        # Creates two arrays for the left and right lists
        left = [0] * num_left
        right = [0] * num_right

        # Fills the new left and right arrays with the words from the original array
        for i in range(0, num_left):
            left[i] = words[begin + i]
        for j in range(0, num_right):
            right[j] = words[mid + j + 1]
        
        # Sets start indices for left, right, and original lists
        i = 0
        j = 0
        k = begin

        while i < num_left and j < num_right:
            if left[i] <= right[j]:
                words[k] = left[i] # Adds the left list's word to the original array if it is less than right word
                i += 1 # Increments to next left word
            else:
                words[k] = right[j] # Adds the right word to the original array if it is is less than the left word
                j += 1 # Increments index to next right word
            k += 1 # Increments the position in the original array

        # After one of the L or R lists is empty, adds the rest of the other list to the original array
        while i < num_left:
            words[k] = left[i]
            i += 1
            k += 1
        
        while j < num_right:
            words[k] = right[j]
            j += 1
            k += 1

        return words
    
    def olelo_search(self, word):
        # Binary search for specific word
        # Sets the start, middle, and end indices for the search array
        word = word.lower() # Ensures word case doesn't conflict with search
        start = 0
        end = len(self.olelo_wordlist) - 1

        while start <= end: # Continues to run until the start index passes the end index
            # Calculates the new middle index
            mid = (start + end) // 2

            # If the middle word is the search word
            if word == self.olelo_wordlist[mid]:
                return True

            # If the search word comes after the middle word
            # sets the start index to search the right half of list
            elif word > self.olelo_wordlist[mid]:
                start = mid + 1
            
            # If the search word comes before the middle,
            # sets the end index to the search left half of list
            else:
                end = mid - 1

        # Returns false if the word is not in list
        return False

    def english_search(self, word):
        # Binary search for specific word
        # Sets the start, middle, and end indices for the search array
        word = word.lower()
        start = 0
        end = len(self.english_wordlist) - 1

        while start <= end: # Continues to run until the start index passes the end index
            # Calculates the new middle index
            mid = (start + end) // 2

            # If the middle word is the search word
            if word == self.english_wordlist[mid]:
                return True

            # If the search word comes after the middle word
            # sets the start index to search the right half of list
            elif word > self.english_wordlist[mid]:
                start = mid + 1
            
            # If the search word comes before the middle,
            # sets the end index to the search left half of list
            else:
                end = mid - 1

        # Returns false if the word is not in list
        return False

        

 