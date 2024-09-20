from olelonode import OleloNode as onode
from olelotree import OleloTree as otree


class main():
    node = onode("Waialua, ʻāina kū pālua i ka laʻi.", "Waialua, land that stands doubly becalmed.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")
    node2 = onode("Hoʻokahi nō lā o ka malihini.", "A stranger only for a day.", "After the first day as a guest, one must help with the work.", "After the first day as a guest, one must help with the work.")
    node3 = onode("Waialua, ʻāina kū pālua i ka laʻi.", "Waialua, land that stands doubly becalmed.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")

    tree = otree()
    tree.insert("Waialua, ʻāina kū pālua i ka laʻi.", "Waialua, land that stands doubly becalmed.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")
    tree.insert("Hoʻokahi nō lā o ka malihini.", "A stranger only for a day.", "After the first day as a guest, one must help with the work.", "After the first day as a guest, one must help with the work.")
    tree.insert("Baialua, ʻāina kū pālua i ka laʻi.", "Baialua, land that stands doubly becalmed.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")
    tree.insert("Waialua, ʻāina kū pālua i ka laʻi.", "Waialua, land that stands doubly becalmed.", "Ua ʻōlelo ʻia ʻo ia me ka mahalo iā Waialua, Oʻahu, kahi e ʻoluʻolu ai ka ʻāina a me ka noho mālie o ka poʻe.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")
    tree.insert("Hoʻokahi nō lā o ka malihini.", "A stranger only for a day.", "Ma hope o ka lā mua ma ke ʻano he malihini, pono kekahi e kōkua i ka hana.", "After the first day as a guest, one must help with the work.")
    tree.insert("Komo mai kāu māpuna hoe.", "Put in your dip of the paddle.", "Hoʻokomo i loko.", "Pitch in.")
    tree.insert("Kūlia i ka nuʻu.", "Strive to reach the highest.", "E hoʻomau i ka hana e loaʻa ai ka pono.", "Continue to strive in order to achieve excellence.")
    tree.insert("Na ka ʻeleu miki.", "The prize goes to the quick one.", "E like me ka ʻōlelo, 'Loaʻa i ka manu mua ka ilo.'", "Similar to the saying, “The early bird gets the worm.”")
    tree.insert("ʻAʻa i ka hula, waiho i ka hilahila i ka hale.", "When one wants to dance the hula, bashfulness should be left at home.", "Mai hilahila. E komo! ʻAʻole pili wale kēia i ka hula. Hiki ke hoʻohana i kēia i nā kūlana a pauke hopohopo kekahi i ke komo ʻana i kekahi hana.", "Don’t be shy. Participate! This does not just pertain to hula. This can be used in all situations when one is apprehensive in participating in an activity.")

    print(tree.successor("Waialua, ʻāina kū pālua i ka laʻi."))
    print(tree.predecessor("Waialua, ʻāina kū pālua i ka laʻi."))
    print(tree.successor("Bleep bloop"))

    result = tree.is_member("Waialua, ʻāina kū pālua i ka laʻi.") # is_member is working properly 
    result2 = tree.is_member("Hoʻokahi nō lā o ka malihini.") # is_member is working properly 
    result3 = tree.is_member("Suprcalifragilisticexpialidocious") # is_member returns false when a phrase not in the tree is passed 

    print(result)
    print(result2)
    print(result3)

    predecessor = tree.predecessor("Baialua, ʻāina kū pālua i ka laʻi.")
    print(predecessor)
    print(tree.root)
    print(tree.predecessor("Hoʻokahi nō lā o ka malihini."))
    print(tree.successor("Hoʻokahi nō lā o ka malihini."))
    print(tree.successor("Baialua, ʻāina kū pālua i ka laʻi."))
    print(tree.predecessor("Waialua, ʻāina kū pālua i ka laʻi."))

    print("Search for English word: becalmed")
    print(node.english_search("becalmed"))
    print("Search for Hawaiian word: Waialua")
    print(node.olelo_search("Waialua"))
    print("Search for English word: ka")
    print(node.english_search("ka"))
    print("Search for Hawaiian word: ka")
    print(node.olelo_search("ka"))

    test = tree.MeHua("Waialua")
    test2 = tree.WithWord("land")

    print("MeHua and WithWord Test")
    print(test)
    print(test2)

    print(node.olelo_wordlist)
    print(node.english_wordlist)

    tree.in_order()
main()
