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

    tree.in_order()

    tree.is_member("Waialua, ʻāina kū pālua i ka laʻi")
main()
