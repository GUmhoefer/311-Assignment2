'''
Driver for OleloTree class.
Author: Gregor Umhoefer
        This class first inserts nodes into an instance of the OleloTree class. It then displays a user menu and prompts the user to enter an option.
        The user can check if a phrase is in the database, return the first alphabetical phrase, return the last alphabetical phrase, return the predecessor or 
        successor of a phrase, insert a phrase, return all of the phrases that contain a word in ʻOlelo Hawaiʻi or in english, or exit the program.
'''

from olelotree import OleloTree as otree

def menu():
    print("\nChoose from the following options:\n")
    print("1. Check if a phrase in ʻOlelo Hawaiʻi is in the database.")
    print("2. Return the phrase that is first in alphabetical order.")
    print("3. Return the phrase that is last in alphabetical order.")
    print("4. Enter a phrase in ʻOlelo Hawaiʻi to return its alphabetical predecessor.")
    print("5. Enter a phrase in ʻOlelo Hawaiʻi to return its alphabetical successor.")
    print("6. Insert a phrase into the database.")
    print("7. Me Hua: Enter a word in ʻOlelo Hawaiʻi and return all of the phrases that contain that word.")
    print("8. With Word: Enter a word in English and return all of the phrases whose translations contain that word.")
    print("9. Print all of the phrases in alphabetical order.")
    print("0. Exit the program.\n")


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

    user_choice = 1

    while user_choice != 0:
        menu()
        user_choice = int(input("Please choose an option: "))

        if user_choice == 1:
            phrase = input("Enter a phrase to search for: ")
            if tree.is_member(phrase):
                print("\nThis is a phrase in the database.\n")
            else:
                print("\nThis is not a phrase in the database.\n")

        elif user_choice == 2:
            print(tree.first())

        elif user_choice == 3:
            print(tree.last())

        elif user_choice == 4:
            phrase = input("Enter a phrase in ʻOlelo Hawaiʻi to return its predecessor: ")
            print("\n")
            print(tree.predecessor(phrase))
        
        elif user_choice == 5:
            phrase = input("Enter a phrase in ʻOlelo Hawaiʻi to return its successor: ")
            print("\n")
            print(tree.successor(phrase))

        elif user_choice == 6:
            print("**Insert a new phrase into the database**")
            print("_________________________________________")
            olelo_phrase = input("Enter the phrase in ʻOlelo Hawaiʻi: ")
            english_phrase = input("Enter the phrase in English: ")
            olelo_exp = input("Enter the explanation in ʻOlelo Hawaiʻi: ")
            english_exp = input("Enter the explanation in English: ")
            print("\n")
            tree.insert(olelo_phrase, english_phrase, olelo_exp, english_exp)

        elif user_choice == 7:
            word = input("Enter a word in ʻOlelo Hawaiʻi to return all of the phrases it occurs in: \n")
            phrases = tree.MeHua(word)
            print("\n")
            if phrases:
                for phrase in phrases:
                    print(phrase)
            else:
                print("No ʻOlelo Hawaiʻi phrases contain this word.")

        elif user_choice == 8:
            word = input("Enter a word in English to return all of the phrases whose translations contain that word: \n")
            phrases = tree.WithWord(word)
            print("\n")
            if phrases:
                for phrase in phrases:
                    print(phrase)
            else:
                print("No English phrases contain this word.")

        elif user_choice == 9:
            print("\n")
            tree.in_order()

        elif user_choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid selection, please try again.\n")
            menu()

OleloDriver()