from olelotree import OleloTree as otree

class OleloDriver():
    tree = otree()
    tree.insert("Waialua, ʻāina kū pālua i ka laʻi.", "Waialua, land that stands doubly becalmed.", "Ua ʻōlelo ʻia ʻo ia me ka mahalo iā Waialua, Oʻahu, kahi e ʻoluʻolu ai ka ʻāina a me ka noho mālie o ka poʻe.", "Said in admiration for Waialua, Oʻahu, where the weather wa usually pleasant and the life of the people tranquil.")
    tree.insert("Hoʻokahi nō lā o ka malihini.", "A stranger only for a day.", "Ma hope o ka lā mua ma ke ʻano he malihini, pono kekahi e kōkua i ka hana.", "After the first day as a guest, one must help with the work.")
    tree.insert("Komo mai kāu māpuna hoe.", "Put in your dip of the paddle.", "Hoʻokomo i loko.", "Pitch in.")
    tree.insert("Kūlia i ka nuʻu.", "Strive to reach the highest.", "E hoʻomau i ka hana e loaʻa ai ka pono.", "Continue to strive in order to achieve excellence.")
    tree.insert("Na ka ʻeleu miki.", "The prize goes to the quick one.", "E like me ka ʻōlelo, 'Loaʻa i ka manu mua ka ilo.'", "Similar to the saying, “The early bird gets the worm.”")
    tree.insert("ʻAʻa i ka hula, waiho i ka hilahila i ka hale.", "When one wants to dance the hula, bashfulness should be left at home.", "Mai hilahila. E komo! ʻAʻole pili wale kēia i ka hula. Hiki ke hoʻohana i kēia i nā kūlana a pauke hopohopo kekahi i ke komo ʻana i kekahi hana.", "Don’t be shy. Participate! This does not just pertain to hula. This can be used in all situations when one is apprehensive in participating in an activity.")
    tree.insert("Hoʻokahi wale nō leo, ua lawa.", "One voice is enough.", "Ke kamaʻilio kekahi, pono nā mea a pau e hoʻolohe. Hiki ke manaʻo hoʻokahi wale nō mea hoʻomanaʻo pono.", "When one speaks, everyone should be listening. It can also mean that only one reminder is necessary.")
    tree.insert("He aliʻi ka ʻāina, he kauā ke kanaka.", "The land is a chief; man is its servant.", "ʻAʻole pono ka ʻāina i ke kanaka, akā pono ke kanaka i ka ʻāina a hana i mea e ola ai. Pono kākou e mālama i ka ʻāina.", "Land has no need for man, but man needs the land and works it for a livelihood. We have to take care of the land.")

    tree.in_order()



OleloDriver()