class OleloNode:
    def __init__(self, phrase_olelo, phrase_english, exp_olelo, exp_english):
        self.phrase_olelo = phrase_olelo.split()
        self.phrase_english = phrase_english.split()
        self.exp_olelo = exp_olelo
        self.exp_english = exp_english

        self.left = None  # Left child node
        self.right = None  # Right child node
        self.parent = None # Pointer to parent node

        self.tree_height = 1  # Stores the height this node's tree

    def __str__(self):
        return f"Phrase in Olelo Hawaiʻi:\n{' '.join(self.phrase_olelo)}\nPhrase in English:\n{' '.join(self.phrase_english)}\nExplanation in Olelo Hawaiʻi:\n{self.exp_olelo}\nExplanation in English:\n{self.exp_english}"