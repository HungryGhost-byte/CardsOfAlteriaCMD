import random
import time
import sys
import pickle


name = input("\n Please enter your first name: ")


# Card worth in Gold
# Common = 1
# Uncommon = 2
# Rare = 4
# Mythic = 10


gold = 1000
# to show current gold value
# print(" - " + name + "'s Total Gold: " + str(gold), "-")

cards_got = 0


class Card:
    def __init__(self, name, number, rarity, text):
        self.name = name
        self.number = number
        self.rarity = rarity
        self.text = text

    def acquired(self):
        print("\n")
        print(" You have acquired: " + self.name)
        time.sleep(0.5)
        print(" This is a " + self.rarity, "card!")
        time.sleep(0.5)

    def dupe(self):
        global gold
        print("\n")
        print(" You have acquired: " + self.name)
        time.sleep(0.5)
        print(" This is a duplicate card!")
        if self.rarity == "Mythic":
            print(" You have acquired 10 gold for " + self.name + " card.")
            gold += 10

        elif self.rarity == "Rare":
            print(" You have acquired 4 gold for " + self.name + " card.")
            gold += 4

        elif self.rarity == "Uncommon":
            print(" You have acquired 2 gold for " + self.name + " card.")
            gold += 2

        else:
            print(" You have acquired 1 gold for " + self.name + " card.")
            gold += 1


# card_unlock checks the out come of random.choice(which pulls from collection dict)
# it first checks if the card == True in dict, to catch any duplicate
# if no dupes, it continues to acquired function
def card_unlock(result):
    global cards_got
    if result == c1:
        check_card = collection["c1"]
        if check_card == True:
            c1.dupe()
        else:
            collection["c1"] = True
            cards_got += 1
            c1.acquired()
    elif result == c2:
        check_card = collection["c2"]
        if check_card == True:
            c2.dupe()
        else:
            collection["c2"] = True
            cards_got += 1
            c2.acquired()
    elif result == c3:
        check_card = collection["c3"]
        if check_card == True:
            c3.dupe()
        else:
            collection["c3"] = True
            cards_got += 1
            c3.acquired()
    elif result == c4:
        check_card = collection["c4"]
        if check_card == True:
            c4.dupe()
        else:
            collection["c4"] = True
            cards_got += 1
            c4.acquired()
    elif result == c5:
        check_card = collection["c5"]
        if check_card == True:
            c5.dupe()
        else:
            collection["c5"] = True
            cards_got += 1
            c5.acquired()
    elif result == c6:
        check_card = collection["c6"]
        if check_card == True:
            c6.dupe()
        else:
            collection["c6"] = True
            cards_got += 1
            c6.acquired()
    elif result == c7:
        check_card = collection["c7"]
        if check_card == True:
            c7.dupe()
        else:
            collection["c7"] = True
            cards_got += 1
            c7.acquired()
    elif result == c8:
        check_card = collection["c8"]
        if check_card == True:
            c8.dupe()
        else:
            collection["c8"] = True
            cards_got += 1
            c8.acquired()
    elif result == c9:
        check_card = collection["c9"]
        if check_card == True:
            c9.dupe()
        else:
            collection["c9"] = True
            cards_got += 1
            c9.acquired()
    elif result == c10:
        check_card = collection["c10"]
        if check_card == True:
            c10.dupe()
        else:
            collection["c10"] = True
            cards_got += 1
            c10.acquired()
    elif result == c11:
        check_card = collection["c11"]
        if check_card == True:
            c11.dupe()
        else:
            collection["c11"] = True
            cards_got += 1
            c11.acquired()
    elif result == c12:
        check_card = collection["c12"]
        if check_card == True:
            c12.dupe()
        else:
            collection["c12"] = True
            cards_got += 1
            c12.acquired()
    elif result == c13:
        check_card = collection["c13"]
        if check_card == True:
            c13.dupe()
        else:
            collection["c13"] = True
            cards_got += 1
            c13.acquired()
    elif result == c14:
        check_card = collection["c14"]
        if check_card == True:
            c14.dupe()
        else:
            collection["c14"] = True
            cards_got += 1
            c14.acquired()
    elif result == c15:
        check_card = collection["c15"]
        if check_card == True:
            c15.dupe()
        else:
            collection["c15"] = True
            cards_got += 1
            c15.acquired()
    elif result == c16:
        check_card = collection["c16"]
        if check_card == True:
            c16.dupe()
        else:
            collection["c16"] = True
            cards_got += 1
            c16.acquired()
    elif result == c17:
        check_card = collection["c17"]
        if check_card == True:
            c17.dupe()
        else:
            collection["c17"] = True
            cards_got += 1
            c17.acquired()
    elif result == c18:
        check_card = collection["c18"]
        if check_card == True:
            c18.dupe()
        else:
            collection["c18"] = True
            cards_got += 1
            c18.acquired()
    elif result == c19:
        check_card = collection["c19"]
        if check_card == True:
            c19.dupe()
        else:
            collection["c19"] = True
            cards_got += 1
            c19.acquired()
    elif result == c20:
        check_card = collection["c20"]
        if check_card == True:
            c20.dupe()
        else:
            collection["c20"] = True
            cards_got += 1
            c20.acquired()
    elif result == c21:
        check_card = collection["c21"]
        if check_card == True:
            c21.dupe()
        else:
            collection["c21"] = True
            cards_got += 1
            c21.acquired()
    elif result == c22:
        check_card = collection["c22"]
        if check_card == True:
            c22.dupe()
        else:
            collection["c22"] = True
            cards_got += 1
            c22.acquired()
    elif result == c23:
        check_card = collection["c23"]
        if check_card == True:
            c23.dupe()
        else:
            collection["c23"] = True
            cards_got += 1
            c23.acquired()
    elif result == c24:
        check_card = collection["c24"]
        if check_card == True:
            c24.dupe()
        else:
            collection["c24"] = True
            cards_got += 1
            c24.acquired()
    elif result == c25:
        check_card = collection["c25"]
        if check_card == True:
            c25.dupe()
        else:
            collection["c25"] = True
            cards_got += 1
            c25.acquired()
    elif result == c26:
        check_card = collection["c26"]
        if check_card == True:
            c26.dupe()
        else:
            collection["c26"] = True
            cards_got += 1
            c26.acquired()
    elif result == c27:
        check_card = collection["c27"]
        if check_card == True:
            c27.dupe()
        else:
            collection["c27"] = True
            cards_got += 1
            c27.acquired()
    elif result == c28:
        check_card = collection["c28"]
        if check_card == True:
            c28.dupe()
        else:
            collection["c28"] = True
            cards_got += 1
            c28.acquired()
    elif result == c29:
        check_card = collection["c29"]
        if check_card == True:
            c29.dupe()
        else:
            collection["c29"] = True
            cards_got += 1
            c29.acquired()
    elif result == c30:
        check_card = collection["c30"]
        if check_card == True:
            c30.dupe()
        else:
            collection["c30"] = True
            cards_got += 1
            c30.acquired()
    elif result == c31:
        check_card = collection["c31"]
        if check_card == True:
            c31.dupe()
        else:
            collection["c31"] = True
            cards_got += 1
            c31.acquired()
    elif result == c32:
        check_card = collection["c32"]
        if check_card == True:
            c32.dupe()
        else:
            collection["c32"] = True
            cards_got += 1
            c32.acquired()
    elif result == c33:
        check_card = collection["c33"]
        if check_card == True:
            c33.dupe()
        else:
            collection["c33"] = True
            cards_got += 1
            c33.acquired()
    elif result == c34:
        check_card = collection["c34"]
        if check_card == True:
            c34.dupe()
        else:
            collection["c34"] = True
            cards_got += 1
            c34.acquired()
    elif result == c35:
        check_card = collection["c35"]
        if check_card == True:
            c35.dupe()
        else:
            collection["c35"] = True
            cards_got += 1
            c35.acquired()
    elif result == c36:
        check_card = collection["c36"]
        if check_card == True:
            c36.dupe()
        else:
            collection["c36"] = True
            cards_got += 1
            c36.acquired()
    elif result == c37:
        check_card = collection["c37"]
        if check_card == True:
            c37.dupe()
        else:
            collection["c37"] = True
            cards_got += 1
            c37.acquired()
    elif result == c38:
        check_card = collection["c38"]
        if check_card == True:
            c38.dupe()
        else:
            collection["c38"] = True
            cards_got += 1
            c38.acquired()
    elif result == c39:
        check_card = collection["c39"]
        if check_card == True:
            c39.dupe()
        else:
            collection["c39"] = True
            cards_got += 1
            c39.acquired()
    elif result == c40:
        check_card = collection["c40"]
        if check_card == True:
            c40.dupe()
        else:
            collection["c40"] = True
            cards_got += 1
            c40.acquired()
    elif result == c41:
        check_card = collection["c41"]
        if check_card == True:
            c41.dupe()
        else:
            collection["c41"] = True
            cards_got += 1
            c41.acquired()
    elif result == c42:
        check_card = collection["c42"]
        if check_card == True:
            c42.dupe()
        else:
            collection["c42"] = True
            cards_got += 1
            c42.acquired()
    elif result == c43:
        check_card = collection["c43"]
        if check_card == True:
            c43.dupe()
        else:
            collection["c43"] = True
            cards_got += 1
            c43.acquired()
    elif result == c44:
        check_card = collection["c44"]
        if check_card == True:
            c44.dupe()
        else:
            collection["c44"] = True
            cards_got += 1
            c44.acquired()
    elif result == c45:
        check_card = collection["c45"]
        if check_card == True:
            c45.dupe()
        else:
            collection["c45"] = True
            cards_got += 1
            c45.acquired()
    elif result == c46:
        check_card = collection["c46"]
        if check_card == True:
            c46.dupe()
        else:
            collection["c46"] = True
            cards_got += 1
            c46.acquired()
    elif result == c47:
        check_card = collection["c47"]
        if check_card == True:
            c47.dupe()
        else:
            collection["c47"] = True
            cards_got += 1
            c47.acquired()
    elif result == c48:
        check_card = collection["c48"]
        if check_card == True:
            c48.dupe()
        else:
            collection["c48"] = True
            cards_got += 1
            c48.acquired()
    elif result == c49:
        check_card = collection["c49"]
        if check_card == True:
            c49.dupe()
        else:
            collection["c49"] = True
            cards_got += 1
            c49.acquired()
    elif result == c50:
        check_card = collection["c50"]
        if check_card == True:
            c50.dupe()
        else:
            collection["c50"] = True
            cards_got += 1
            c50.acquired()
    else:
        return None


################ S E A S O N   1   C A R D S ##################


c1 = Card("Skeletal Knight", "1", "Common", "When the Aldrus Empire fell, its vast army was affected \n"
                                            " by a terrible curse. They were forced to wonder the lands\n "
                                            " aimlessly, even in death.")
c2 = Card("Mountain Fairy", "2", "Common", "In the western mountains of the Edeera Region, these fairies\n"
                                           " call home. Unlike other fairies, they are accustomed to \n"
                                           " humans. It isn't out of place for them to find them in the local\n"
                                           " towns and cities.")
c3 = Card("Dwarven Storyteller", "3", "Common", "If there is one thing Dwarves are known for besides Smithing,\n"
                                                " it's a good tale. Many have made a profession of traveling\n"
                                                " far and wide, telling tales of wonders and mystery's.")
c4 = Card("Honest Rogue", "4", "Uncommon", "A Rogue by profession isn't known to be honest, but you always\n"
                                           " get that one...")
c5 = Card("Valia Knight", "5", "Uncommon", "A Knight of the Valia Kingdom, north of Dragon Valley. From the age\n"
                                           " of ten, they enter into a life of servitude to their country, and\n"
                                           " undergo the most rigorous of training")
c6 = Card("Forest Dragon", "6", "Rare", "Dragons are not a rare sight, many of which make their homes deep\n"
                                        " within forests.")
c7 = Card("Wandering Ghost", "7", "Common", "Ghosts that wonder the world usually do so for good reason. It\n"
                                            " is not natural that they do not pass on in death.")
c8 = Card("Whispering Tree Branch", "8", "Common", "There are tales of certain trees in the forests, that\n"
                                                   " when listened to, speak of the secrets carried to them\n"
                                                   " on the wind.")
c9 = Card("Nomadic Merchant", "9", "Common", "Merchants hail from every corner of the land and are vital\n"
                                             " for economies.")
c10 = Card("Sand Giant", "10", "Uncommon", "These beings are found within the deserts of Ashuu, casting \n"
                                           " shade across wide areas from their humongous size. Although \n"
                                           " they are a sight to behold, going near one is certain death.")
c11 = Card("Woodland Prowler", "11", "Uncommon", "Wild cat-like creatures the size of an adult human - they\n"
                                                 " have an aggressive nature and move only during the night.")
c12 = Card("Isazahl, The Slumbering Wizard", "12", "Common", "A great wizard, but a lazy one. His magic was\n"
                                                             " so powerful that he created countless copies\n"
                                                             " of himself to work on his projects while he\n"
                                                             " took extended naps.")
c13 = Card("Lost City of The Sunken Sands", "13", "Rare", "It is still a matter of firey debate whether the\n"
                                                          " mythical Lost City actually exists or is simply\n"
                                                          " the product of good storytelling. Some have claimed\n"
                                                          " to have seen it with their own eyes.")
c14 = Card("Tardy Blacksmith", "14", "Common", "It's not always the case where someones name reflects their \n"
                                               " habits, but here we are.")
c15 = Card("Babbling Brook", "15", "Common", "They say that people are buried alive near streams, so their \n"
                                             " wailing sounds like its coming from the waters. Don't ask \n"
                                             " who \"they\" are.")
c16 = Card("Witch's Cauldron", "16", "Common", "It's what a witch usually uses to craft her potions and \n"
                                               " perfect her spells.")
c17 = Card("Forbidden Wizard's Parchment", "17", "Uncommon", "Sounds cool, doesn't it.")
c18 = Card("King Ugg the Ape", "18", "Uncommon", "A mighty gorilla that rules the jungles in southern \n"
                                                 " Bananaram.")
c19 = Card("Scriptures of The Five Moons", "19", "Rare", "Each moon is said to be symbolic of the five \n"
                                                         " wizards that hailed from Stonebrook Castle \n"
                                                         " University.")
c20 = Card("Skeletal Knight", "20", "Common", "Whenever the undead is concerned, you can be sure a curse \n"
                                              " is not far behind. These")
c21 = Card("Grim Reaper the Sleeper", "21", "Common", "Don't let the rhymes fool you, when the Reaper wakes, \n"
                                                      " things get a bit morbid.")
c22 = Card("Compass of the Misty North", "22", "Common", "This magical compass is said to point towards the \n"
                                                         " lost treasure of Peg-leg Percy Plop. He was a poor \n"
                                                         " pirate, in wealth and taste.")
c23 = Card("Queen Kit the Cat", "23", "Uncommon", "Home of the sewer strays of Dimdim City, she is able \n"
                                                  " to speak the common tongue and translate between humans \n"
                                                  " and regular cats.")
c24 = Card("Raging Bear-owl", "24", "Uncommon", "It's still not known whether this abomination was created or \n"
                                                " occurred naturally. Don't let the innocent owl-like face \n"
                                                " deceive you, it is a vicious thing.")
c25 = Card("Sword of the Sultan", "25", "Common", "There are many sultans, thus there are many swords.")
c26 = Card("The Ghost Ship - Grim Patron", "26", "Mythic", "This ship of death is large in size and majesty. \n"
                                                           " Appearing on foggy nights deep at sea, this \n"
                                                           " vessel is said to carry on it the riches of all \n"
                                                           " past empires. There is also an item on this ship \n"
                                                           " that is said to give a wish to any who touch it.")
c27 = Card("Cackling Ravens", "27", "Common", "Dark as the night, they wait among the wounded before it's safe \n"
                                              " to eat. For those poor unfortunate souls, the cackling of the \n"
                                              " ravens is the last thing they will ever hear.")
c28 = Card("Graveyard Redcap", "28", "Common", "These Redcaps are grave-robbing goblins that travel in packs. \n"
                                               " Should you stumble across one, run. They will not hesitate \n"
                                               " to kill and loot your corpse.")
c29 = Card("Bridge Troll", "29", "Uncommon", "While not a common sight, bridge trolls are becoming more \n"
                                             " numerous in number as threatening travelers for their gold \n"
                                             " is easy income.")
c30 = Card("The Kings Chessboard", "30", "Uncommon", "Chess - a popular game among royalty. In some lands, \n"
                                                     " wars are not fought on the battle-field, but on the \n"
                                                     " board.")
c31 = Card("Crocodile River", "31", "Uncommon", "Those guilty of crimes are dropped into this \n"
                                                " crocodile infested river. the crocodiles themselves \n"
                                                " are plump from the enemies of the Zumaama Kingdom.")
c32 = Card("Sand Pirate marauder", "32", "Uncommon", "The sands are as vast as the oceans in Alteria. \n"
                                                     " Magical ships sail the sands, but it is the  \n"
                                                     " marauders that will be found far from borders of \n"
                                                     " kingdoms that pay for their heads.")
c33 = Card("Gold-fin, the Pirate King", "33", "Rare", "This Shark-man hybrid has made a fearsome \n"
                                                      " reputation of himself. He was rich before \n"
                                                      " pirating - he just does it for the pleasure.")
c34 = Card("Magic Mirror", "34", "Common", "The mirror shows the reflection you want to see.")
c35 = Card("Stairs to the Underworld", "35", "Common", "Cold and grey, only the most unfortunate find \n"
                                                       " themselves here.")
c36 = Card("Bell of the Misty Mire", "36", "Common", "The bell that never stops ringing. If you are close \n"
                                                     " enough to hear it, you are already too deep in the \n"
                                                     " swamp to find a way out.")
c37 = Card("Secret Note", "37", "Uncommon", "The writing is written in code, but at the bottom it is \n"
                                            " is signed \"Ms. Mowz\".")
c38 = Card("Sorceress Mervania", "38", "Uncommon", "A powerful spell-caster, her age is unknown, but she \n"
                                                   " has been referenced in tomes tha tare over a thousand \n"
                                                   " years old. Her castle reaches out high above the forest \n"
                                                   " it sits in.")
c39 = Card("Ring of Titrel", "39", "Uncommon", "Wanted by many, this ring controls a mysterious cauldron \n"
                                               " that is said to play a part in brining forth the end of the \n"
                                               " world.")
c40 = Card("Djinn", "40", "Common", "Mischievous spirits that cannot be seen with the naked eye. \n"
                                    " Your socks going missing again could be explained.")
c41 = Card("Corrupted Ashbringer", "41", "Mythic", "A sword once infused with light, now drenched in \n"
                                                   " deceit and darkness. Whispers can be heard from \n"
                                                   " the sword from anyone who wields it.")
c42 = Card("Golden Griffin", "42", "Common", "These creatures are hunted extensively for their golden feathers.")
c43 = Card("Dragon Egg", "43", "Common", "Dragon eggs are a delicacy for the rich and powerful")
c44 = Card("Mewtwo", "44", "Uncommon", "One of its kind. This creature was said to have been created \n"
                                       " in a lab.")
c45 = Card("Dark Crow Inn", "45", "Uncommon", "Nestled in the dark corner of the grand city of Ultime, \n"
                                              " the patrons of this busy pub come in all shapes, sizes \n"
                                              " and species.")
c46 = Card("Pirate Town - Skullmoore", "46", "Rare", "The largest port in Alteria for trade - ruled by \n"
                                        " no kingdom, and of pirates! If there is a place \n"
                                        " where pirates are safe, it's here. As for anyone else? \n"
                                                     " That's another matter.")
c47 = Card("Kokiri Sword", "47", "Common", "A crude sword made of wood. It's rather small to be of any \n"
                                           " real use.")
c48 = Card("Ivory Succubus", "48", "Uncommon", "These elusive creatures travel only by the light of a \n"
                                               " full moon. Their beauty is unmatched.")
c49 = Card("Grimmswald, the Mad", "49", "Rare", "The werewolf was said to once be a man from a long, \n"
                                                " royal lineage. The savage nature has overtaken any \n"
                                                " semblance of humanity that might have remained.")
c50 = Card("Queen of the Dead", "50", "Mythic", "As old as time itself, ruler of the Underworld and \n"
                                                " equaliser of all things. She is nameless, but she is \n"
                                                " feared by all. Her empire is endless and ever growing.")
c51 = Card("The Ultimate Card - Legendary", "51", "Legendary", "Unheard of.")


# Index cards in a dict with bool to signify if card has been collected yet or not
collection = {
    "c1": False,
    "c2": False,
    "c3": False,
    "c4": False,
    "c5": False,
    "c6": False,
    "c7": False,
    "c8": False,
    "c9": False,
    "c10": False,
    "c11": False,
    "c12": False,
    "c13": False,
    "c14": False,
    "c15": False,
    "c16": False,
    "c17": False,
    "c18": False,
    "c19": False,
    "c20": False,
    "c21": False,
    "c22": False,
    "c23": False,
    "c24": False,
    "c25": False,
    "c26": False,
    "c27": False,
    "c28": False,
    "c29": False,
    "c30": False,
    "c31": False,
    "c32": False,
    "c33": False,
    "c34": False,
    "c35": False,
    "c36": False,
    "c37": False,
    "c38": False,
    "c39": False,
    "c40": False,
    "c41": False,
    "c42": False,
    "c43": False,
    "c44": False,
    "c45": False,
    "c46": False,
    "c47": False,
    "c48": False,
    "c49": False,
    "c50": False,
    "C51": False
}
# index number of cards in a list for random.choice to pull from
cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13,
         c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25,
         c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37,
         c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49,
         c50, c51]


def five_pack():
    print("\n")
    input(" Press any key to open a pack containing 5 cards!")
    print("\n")
    count = 0
    while count != 5:
        roll_dice()
        # result = random.choice(cards)
        # card_unlock(result)
        print("\n")
        count += 1
        time.sleep(0.5)


def ten_pack():
    print("\n")
    input(" Press any key to open a pack containing 10 cards!")
    print("\n")
    count = 0
    while count != 10:
        roll_dice()
        # result = random.choice(cards)
        # card_unlock(result)
        print("\n")
        count += 1
        time.sleep(0.5)


def mythic():
    m = random.choice(cards)
    while m.rarity != "Mythic":
        m = random.choice(cards)
    else:
        input(" Press any key to reveal a Mythic card!")
        card_unlock(m)


def cant_afford():
    print(" Sorry, it seems you don't have enough gold for that!\n")
    time.sleep(0.5)
    print(" Try something else!\n")


def card_album():
    global cards_got
    print("\n\n")
    print("      ~~ " + name + "'s Card Collection ~~ ")
    print("\n\n\n")
    if collection["c1"] is True:
        print(" Name: ", cards[0].name, "\n Number: ", cards[0].number,
              "\n Rarity: ", cards[0].rarity, "\n Text: ", cards[0].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[0].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c2"] is True:
        print(" Name: ", cards[1].name, "\n Number: ", cards[1].number,
              "\n Rarity: ", cards[1].rarity, "\n Text: ", cards[1].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[1].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c3"] is True:
        print(" Name: ", cards[2].name, "\n Number: ", cards[2].number,
              "\n Rarity: ", cards[2].rarity, "\n Text: ", cards[2].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[2].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c4"] is True:
        print(" Name: ", cards[3].name, "\n Number: ", cards[3].number,
              "\n Rarity: ", cards[3].rarity, "\n Text: ", cards[3].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[3].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c5"] is True:
        print(" Name: ", cards[4].name, "\n Number: ", cards[4].number,
              "\n Rarity: ", cards[4].rarity, "\n Text: ", cards[4].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[4].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c6"] is True:
        print(" Name: ", cards[5].name, "\n Number: ", cards[5].number,
              "\n Rarity: ", cards[5].rarity, "\n Text: ", cards[5].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[5].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c7"] is True:
        print(" Name: ", cards[6].name, "\n Number: ", cards[6].number,
              "\n Rarity: ", cards[6].rarity, "\n Text: ", cards[6].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[6].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c8"] is True:
        print(" Name: ", cards[7].name, "\n Number: ", cards[7].number,
              "\n Rarity: ", cards[7].rarity, "\n Text: ", cards[7].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[7].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c9"] is True:
        print(" Name: ", cards[8].name, "\n Number: ", cards[8].number,
              "\n Rarity: ", cards[8].rarity, "\n Text: ", cards[8].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[8].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c10"] is True:
        print(" Name: ", cards[9].name, "\n Number: ", cards[9].number,
              "\n Rarity: ", cards[9].rarity, "\n Text: ", cards[9].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[9].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c11"] is True:
        print(" Name: ", cards[10].name, "\n Number: ", cards[10].number,
              "\n Rarity: ", cards[10].rarity, "\n Text: ", cards[10].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[10].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c12"] is True:
        print(" Name: ", cards[11].name, "\n Number: ", cards[11].number,
              "\n Rarity: ", cards[11].rarity, "\n Text: ", cards[11].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[11].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c13"] is True:
        print(" Name: ", cards[12].name, "\n Number: ", cards[12].number,
              "\n Rarity: ", cards[12].rarity, "\n Text: ", cards[12].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[12].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c14"] is True:
        print(" Name: ", cards[13].name, "\n Number: ", cards[13].number,
              "\n Rarity: ", cards[13].rarity, "\n Text: ", cards[13].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[13].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c15"] is True:
        print(" Name: ", cards[14].name, "\n Number: ", cards[14].number,
              "\n Rarity: ", cards[14].rarity, "\n Text: ", cards[14].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[14].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c16"] is True:
        print(" Name: ", cards[15].name, "\n Number: ", cards[15].number,
              "\n Rarity: ", cards[15].rarity, "\n Text: ", cards[15].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[15].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c17"] is True:
        print(" Name: ", cards[16].name, "\n Number: ", cards[16].number,
              "\n Rarity: ", cards[16].rarity, "\n Text: ", cards[16].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[16].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c18"] is True:
        print(" Name: ", cards[17].name, "\n Number: ", cards[17].number,
              "\n Rarity: ", cards[17].rarity, "\n Text: ", cards[17].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[17].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c19"] is True:
        print(" Name: ", cards[18].name, "\n Number: ", cards[18].number,
              "\n Rarity: ", cards[18].rarity, "\n Text: ", cards[18].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[18].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c20"] is True:
        print(" Name: ", cards[19].name, "\n Number: ", cards[19].number,
              "\n Rarity: ", cards[19].rarity, "\n Text: ", cards[19].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[19].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c21"] is True:
        print(" Name: ", cards[20].name, "\n Number: ", cards[20].number,
              "\n Rarity: ", cards[20].rarity, "\n Text: ", cards[20].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[20].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c22"] is True:
        print(" Name: ", cards[21].name, "\n Number: ", cards[21].number,
              "\n Rarity: ", cards[21].rarity, "\n Text: ", cards[21].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[21].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c23"] is True:
        print(" Name: ", cards[22].name, "\n Number: ", cards[22].number,
              "\n Rarity: ", cards[22].rarity, "\n Text: ", cards[22].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[22].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c24"] is True:
        print(" Name: ", cards[23].name, "\n Number: ", cards[23].number,
              "\n Rarity: ", cards[23].rarity, "\n Text: ", cards[23].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[23].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c25"] is True:
        print(" Name: ", cards[24].name, "\n Number: ", cards[24].number,
              "\n Rarity: ", cards[24].rarity, "\n Text: ", cards[24].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[24].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c26"] is True:
        print(" Name: ", cards[25].name, "\n Number: ", cards[25].number,
              "\n Rarity: ", cards[25].rarity, "\n Text: ", cards[25].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[25].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c27"] is True:
        print(" Name: ", cards[26].name, "\n Number: ", cards[26].number,
              "\n Rarity: ", cards[26].rarity, "\n Text: ", cards[26].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[26].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c28"] is True:
        print(" Name: ", cards[27].name, "\n Number: ", cards[27].number,
              "\n Rarity: ", cards[27].rarity, "\n Text: ", cards[27].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[27].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c29"] is True:
        print(" Name: ", cards[28].name, "\n Number: ", cards[28].number,
              "\n Rarity: ", cards[28].rarity, "\n Text: ", cards[28].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[28].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c30"] is True:
        print(" Name: ", cards[29].name, "\n Number: ", cards[29].number,
              "\n Rarity: ", cards[29].rarity, "\n Text: ", cards[29].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[29].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c31"] is True:
        print(" Name: ", cards[30].name, "\n Number: ", cards[30].number,
              "\n Rarity: ", cards[30].rarity, "\n Text: ", cards[30].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[30].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c32"] is True:
        print(" Name: ", cards[31].name, "\n Number: ", cards[31].number,
              "\n Rarity: ", cards[31].rarity, "\n Text: ", cards[31].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[31].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c33"] is True:
        print(" Name: ", cards[32].name, "\n Number: ", cards[32].number,
              "\n Rarity: ", cards[32].rarity, "\n Text: ", cards[32].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[32].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c34"] is True:
        print(" Name: ", cards[33].name, "\n Number: ", cards[33].number,
              "\n Rarity: ", cards[33].rarity, "\n Text: ", cards[33].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[33].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c35"] is True:
        print(" Name: ", cards[34].name, "\n Number: ", cards[34].number,
              "\n Rarity: ", cards[34].rarity, "\n Text: ", cards[34].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[34].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c36"] is True:
        print(" Name: ", cards[35].name, "\n Number: ", cards[35].number,
              "\n Rarity: ", cards[35].rarity, "\n Text: ", cards[35].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[35].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c37"] is True:
        print(" Name: ", cards[36].name, "\n Number: ", cards[36].number,
              "\n Rarity: ", cards[36].rarity, "\n Text: ", cards[36].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[36].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c38"] is True:
        print(" Name: ", cards[37].name, "\n Number: ", cards[37].number,
              "\n Rarity: ", cards[37].rarity, "\n Text: ", cards[37].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[37].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c39"] is True:
        print(" Name: ", cards[38].name, "\n Number: ", cards[38].number,
              "\n Rarity: ", cards[38].rarity, "\n Text: ", cards[38].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[38].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c40"] is True:
        print(" Name: ", cards[39].name, "\n Number: ", cards[39].number,
              "\n Rarity: ", cards[39].rarity, "\n Text: ", cards[39].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[39].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c41"] is True:
        print(" Name: ", cards[40].name, "\n Number: ", cards[40].number,
              "\n Rarity: ", cards[40].rarity, "\n Text: ", cards[40].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[40].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c42"] is True:
        print(" Name: ", cards[41].name, "\n Number: ", cards[41].number,
              "\n Rarity: ", cards[41].rarity, "\n Text: ", cards[41].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[41].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c43"] is True:
        print(" Name: ", cards[42].name, "\n Number: ", cards[42].number,
              "\n Rarity: ", cards[42].rarity, "\n Text: ", cards[42].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[42].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c44"] is True:
        print(" Name: ", cards[43].name, "\n Number: ", cards[43].number,
              "\n Rarity: ", cards[43].rarity, "\n Text: ", cards[43].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[43].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c45"] is True:
        print(" Name: ", cards[44].name, "\n Number: ", cards[44].number,
              "\n Rarity: ", cards[44].rarity, "\n Text: ", cards[44].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[44].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c46"] is True:
        print(" Name: ", cards[45].name, "\n Number: ", cards[45].number,
              "\n Rarity: ", cards[45].rarity, "\n Text: ", cards[45].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[45].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c47"] is True:
        print(" Name: ", cards[46].name, "\n Number: ", cards[46].number,
              "\n Rarity: ", cards[46].rarity, "\n Text: ", cards[46].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[46].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c48"] is True:
        print(" Name: ", cards[47].name, "\n Number: ", cards[47].number,
              "\n Rarity: ", cards[47].rarity, "\n Text: ", cards[47].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[47].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c49"] is True:
        print(" Name: ", cards[48].name, "\n Number: ", cards[48].number,
              "\n Rarity: ", cards[48].rarity, "\n Text: ", cards[48].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[48].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if collection["c50"] is True:
        print(" Name: ", cards[49].name, "\n Number: ", cards[49].number,
              "\n Rarity: ", cards[49].rarity, "\n Text: ", cards[49].text)
    else:
        print(" - Card Not Collected -")
        print(" Name: Unknown", "\n Number: ", cards[49].number,
              "\n Rarity: Unknown", "\n Text: Unknown")
    print("\n")
    if cards_got == 50:
        print(" Name: ", cards[50].name, "\n Number: ", cards[50].number,
              "\n Rarity: ", cards[50].rarity, "\n Text: ", cards[50].text)
    print("\n\n\n")
# Card counter
    if cards_got == 50:
        print("You have collected 51/51 cards.")
    else:
        print(" You have collected " + str(cards_got) + "/50 cards.\n\n")

    back_to_menu = input(" Press Any Key for Main Menu")
    print("\n\n\n")
    main_menu()
    print("~~ ----------------------- ~~")


####################### S  H  O  P ########################


def shop():
    global gold
    print("\n\n\n")
    print("                      ~~~")
    time.sleep(0.5)
    print("     ~~ Hayaliyah's Wonderous Card Shop ~~")
    time.sleep(0.5)
    print("                      ~~~")
    time.sleep(0.5)
    print("\n\n")
    print(" Welcome! Please, come in to my little shop of wonders. Got lots of \n"
          " gold and don't know what to spend it on? Then you've come to \n"
          " the right place! Please, check the offers below and see if anything catches \n"
          " your eye...")
    time.sleep(1.5)
    print("\n\n")
    print(" .~ For Sale ~.\n 1. Single Random Card: 10 Gold\n 2. Card Pack(5): 50 Gold\n "
          "3: Card Pack(10): 100 Gold\n 4: Single Mythic Card: 500 Gold\n 5. Back to Main Menu\n\n")
    time.sleep(0.5)
    print(" - " + name + "'s Total Gold: " + str(gold), "-")
    print(" -------------------------")
    time.sleep(0.5)
    print("\n")
    while True:
        time.sleep(0.5)
        buy = input(" What would you like to buy?\n < Select by inputting corresponding number >\n\n")
        if buy == "1":
            if gold < int(10):
                time.sleep(0.5)
                cant_afford()
                print("\n")
            else:
                time.sleep(0.5)
                gold = gold - 10
                roll_dice()
                print("\n")
                time.sleep(2.0)
                print(" .~ For Sale ~.\n 1. Single Random Card: 10 Gold\n 2. Card Pack(5): 50 Gold\n "
                      "3: Card Pack(10): 100 Gold\n 4: Single Mythic Card: 500 Gold\n 5. Back to Main Menu\n\n")
                time.sleep(0.5)
                print(" - " + name + "'s Total Gold: " + str(gold), "-")
                print("\n")
        elif buy == "2":
            if gold < int(50):
                time.sleep(0.5)
                cant_afford()
                print("\n")
            else:
                time.sleep(0.5)
                gold = gold - 50
                five_pack()
                print("\n")
                time.sleep(2.0)
                print(" .~ For Sale ~.\n 1. Single Random Card: 10 Gold\n 2. Card Pack(5): 50 Gold\n "
                      "3: Card Pack(10): 100 Gold\n 4: Single Mythic Card: 500 Gold\n 5. Back to Main Menu\n\n")
                time.sleep(0.5)
                print(" - " + name + "'s Total Gold: " + str(gold), "-")
                print("\n")
        elif buy == "3":
            if gold < int(100):
                time.sleep(0.5)
                cant_afford()
                print("\n")
            else:
                time.sleep(0.5)
                gold = gold - 100
                ten_pack()
                print("\n")
                time.sleep(2.0)
                print(" .~ For Sale ~.\n 1. Single Random Card: 10 Gold\n 2. Card Pack(5): 50 Gold\n "
                      "3: Card Pack(10): 100 Gold\n 4: Single Mythic Card: 500 Gold\n 5. Back to Main Menu\n\n")
                time.sleep(0.5)
                print(" - " + name + "'s Total Gold: " + str(gold), "-")
                print("\n")
        elif buy == "4":
            if gold < int(500):
                time.sleep(0.5)
                cant_afford()
                print("\n")
            else:
                time.sleep(0.5)
                gold = gold - 500
                mythic()
                print("\n")
                time.sleep(2.0)
                print(" .~ For Sale ~.\n 1. Single Random Card: 10 Gold\n 2. Card Pack(5): 50 Gold\n "
                      "3: Card Pack(10): 100 Gold\n 4: Single Mythic Card: 500 Gold\n 5. Back to Main Menu\n\n")
                time.sleep(0.5)
                print(" - " + name + "'s Total Gold: " + str(gold), "-")
                print("\n")
        elif buy == "5":
            main_menu()
        else:
            pass


#################### M A I N    M E N U #######################


def main_menu():
    print("\n\n\n")
    print("                            ~~~                   ")
    print("")
    print("         ~~ ~ C A R D S   O F   A L T E R I A ~ ~~")
    print("")
    print("                            ~~~                   ")
    print("\n")
    print("                   Created by Arrian Aziz         ")
    print("                   ----------------------")
    print("\n")
    print("          - A simple card-collecting adventure game -")
    print("\n\n\n")

    start = input(" 1. Start Adventure\n 2. Card Collection\n 3. Shop\n\n\n\n 4. Save \n"
                  " 5. Load\n 6. Exit\n< Select by inputting "
                  "corresponding number >\n\n")

    if start == "1":
        main_game()

    elif start == "2":
        legendary()
        card_album()

    elif start == "3":
        shop()

    elif start == "4":
        time.sleep(0.5)
        progress = input(" Would you like to save your progress?(y/n)")
        if progress == "Y" or progress == "y":
            slow = " Saving...\n"
            for l in slow:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.2)
            save()
            time.sleep(1.5)
            print(" Save complete!")
            time.sleep(1.5)
            main_menu()

        else:
            main_menu()

    elif start == "5":
        time.sleep(0.5)
        progress = input(" Would you like to load your file?(y/n)")
        if progress == "Y" or progress == "y":
            slow = " Loading...\n"
            for l in slow:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(0.2)
            load()
            time.sleep(1.5)
            print(" Load complete!")
            time.sleep(1.5)
            main_menu()

    elif start == "6":
        time.sleep(0.5)
        print(" Farewell...")
        time.sleep(1.5)
        sys.exit()

    else:
        pass

###############  SAVE AND LOAD FUNCTION  ##################
def save():
    global collection, gold, name, cards_got
    pickle.dump(collection, open("savefile1.txt", "wb"))
    pickle.dump(gold, open("savefile2.txt", "wb"))
    pickle.dump(name, open("savefile3.txt", "wb"))
    pickle.dump(cards_got, open("savefile4.txt", "wb"))


def load():
    global collection, gold, name, cards_got
    collection = pickle.load(open("savefile1.txt", "rb"))
    gold = pickle.load(open("savefile2.txt", "rb"))
    name = pickle.load(open("savefile3.txt", "rb"))
    cards_got = pickle.load(open("savefile4.txt", "rb"))


def legendary():
    global cards_got
    if cards_got == 50:
        time.sleep(0.5)
        print("\nYou did it! You collected all the cards. Here's a gift.")
        time.sleep(2.0)
        c51.acquired()
        time.sleep(4.0)

    else:
        pass

# Random roll for a card function
def roll_dice():
    result = random.choice(cards)
    while result.name != "The Ultimate Card - Legendary":
        card_unlock(result)
        break
    else:
        pass


###############################################################


# Main story blocks are in this dictionary. All story texts are pulled from here.
storychoices = {
"B1":"You stand up and dust off your clothes. Your head still feels dizzy as you try to look around,\n"
     "you find yourself at the edge of a forest. Ahead of you in the clearing is a large town of stone and spires.\n"
     "Just then, you notice some rustling in the bushes near you.\nWhat do you choose?\n\n",
"B1b":"As you slowly near the bush, a tiny, furry little creature darts out and away,\ncausing you to fall back in "
      "surprise.  Feeling foolish for being jumpy,\nyou pick yourself up, and that's when you see it. Something else, "
      "in the bushes.\nYou reach in and grab a red gem stone. It looks to be worth something so you pocket it quickly.\n"
      "You decide to quickly head for town.\n\n",
"B2":"As you make it to the "
     "large open gates of the town, you try to catch your breath.\nYour eyes widen as it hits you: the smell of spices, "
     "the wash of colours and the hustle and bustle of the traders on the street.\nAs you walk around, a sign catches "
     "your eye.\nWhat do you choose?\n\n",
"B2a":"You follow some winding stone steps up along a tower to the top then pass\nthrough some hanging beads into a "
      "rather small room full of cushions and\nincense candles. In the middle is a balding dwarf, with his hands over "
      "a crystal ball\nin front of him. He looks up at you.\n“Nice view from up here, eh? But I don’t think you’re "
      "here for the view,”" " " + name + " " "“.\nHow do I know your name?” He chuckles.\n“I know all.” He very mysteriously "
                                     "hovers his hands over his ball as he says this.\n“Now, what do you want?”\n\n",
"B2aa":"“Now listen here you little shit. You wanna get smart with me?\nWell, hows this for a fortune reading?”\nThe "
       "Dwarf throws one of his crystal balls. With a thud,\nit connects squarely on your forehead, sending you "
       "hurtling\nout and off the edge of the stairs sending you to your untimtely demise.\nGame over.\n\n",
"B2ab":"“Slow down. First I wanna see some coin.  What's that? You're dirt poor?\nThen I can't help ya, now scram, "
       "before I start flingin' my balls around.”\nThe Dwarf gets impatient with your exit and decided to help but "
       "rolling\ninto a ball and slamming into you,sending you hurtling out and off the edge of the tower.  "
       "You die.\nGame over.\n\n",
"B2c":"“Psst, hey, you! Over here”\nA hooded figure standing under a nearby archway beckons you over.\n“You look "
      "lost.  Well I can help you if you help me,\nunderstand?  I can tell you aren’t from around here.\n "
      "I can get you home, no problem.  All you have to do is\nmake sure this gets delivered to an annoying old man "
      "outside of town.”  He tries to\nhand you a parcel.  What do you do?\n\n",
"B3":"You decide to head for the Inn.  While a short walk away, it was a little tricky\nto find as it was nestled in "
     "a dark pocket of town, snuggly between other shops.\nThe tavern’s wooden sign creeks back and forth as you "
     "enter.  The place is packed, with singing and laughing,\nbut you cannot help but catch the glare of others; one "
     "in particular, sitting in the\nback-left corner with a cowl covering most of their face and the hilt of a dagger "
     "playing between their fingers.\nAs you get to the bar, a small woman springs up, cleaning the fog from her "
     "spectacles with her apron.\n“Deary me, it gets so hot in here you could roast a boar!  What can I do you with, "
     "my love?” she says to you.\n\n",
"B3b":"You want to order a drink but realise you have no money. There is a mug filled to the brim "
                  "which looks untouched.\nYou decide to take a chance. You grab it and chug it down.\nIt probably "
                  "wasn't the best idea to drink the contents of something you don't know of.\nYou feel a splitting "
                  "headache and the world goes dark around you.\nThus ends your journey, thrown out and left for dead "
                  "in a dark alley.\nGame over.\n\n",
"B4":"“You don’t know where you are? Oh goodness me. Looks like we got another one.\nYou’re not the first to come "
     "in here asking that lately, and I fear you may not be the last.”\nShe sighs out of concern for you.\n“This "
     "here is the town of Ultime, second only to the grand city of\nKorith in all the lands of Alteria.  But I "
     "suppose you haven’t\na clue what I’m on about, just like the others.”\nRubbing her chin, she gets lost in "
     "thought for a moment.\n“I guess there’s nothin’ for it. He’ll hate me but I’ll deal with that old wart later.\n"
     "What did you say your name was?"" " + name + "? What a lovely name, dear. There is a hermit who lives just\n"
                                                   "outside of town.  He don’t like bein' bothered but he’ll know "
                                                   "how to help.  Just tell him Nettle sent you.\nAnd before you go, "
                                                   "take this map, I have his location marked out for you. Don't get "
                                                   "lost!”\n\n",
"B4b":"“Psst, hey, you! Over here”\nThe hooded figure you saw staring at you from the Inn was standing under a nearby "
      "archway.\n“Couldn’t help over-hearing you need help.  Well I can help you if you help me, understand?\nI know "
      "you’re lost, you aren’t from around here.\nI can get you home, no problem.  All you have to do is make sure "
      "this gets delivered to an annoying old man outside of town.”\nHe tries to hand you a parcel.  What do you do?\n\n",
"B4c":"“You refuse? Not very smart. See, we have an issue now. I can't let anyone know about this package,\nso I'm "
      "afraid I can't let you leave here alive.”\nThe man opens his palm towards you and blows strange dust in "
      "your face. "
      "Before you can react, you feel your feet\nget heavy and your eyes close.  You are left for dead in a cold, "
      "dark alley.\nGame over.\n\n",
"B5":"You find yourself back outside of town, walking across a lush green hill,\nheading for the X marked on your map "
     "by Nettle.  You see smoke drifting lazily\ninto the blue sky and as you get nearer, a half-domed house appears.  "
     "You knock on the door,\nbut there is no answer. What do you choose?\n\n",
"B5a":"You decide to do as the shady man says.  Before you know it, you are knocking on the\ndoor to the hermit’s "
      "house just outside of town.\nAn old man opens the door and screams in delight.\n“My pie has arrived! Out of "
      "my way!”\nHe snatches the parcel from you and unwraps it wildly.  Inside is a pie which he eats in one gulp.  "
      "His face turns green and he goes cross-eyed.\n“P-poison…” he mutters as he falls dead in front of you.\nYou "
      "hear screams as a few onlookers have witnessed what just happened.\nYou panic, quickly stumble out of the way, "
      "and scrap your knees as you pick yourself up and run.\nYou do not have time to think of where you are heading, "
      "but you run as hard as you can, not stopping for a second.\nYour eyes get heavy, then everything goes "
      "dark.\nWhen your eyes open, you don’t know how much time\nhas passed or where you are.  You are no longer in "
      "the green fields outside Ultime, quite the opposite in fact.\nYou find yourself amid structures of stone from "
      "a civilisation of past.\nThere are decaying archways and bridges over swamps.  Houses without walls, and "
      "the constant, faintly echoing cries of the lost souls bound to this\naccursed place.  A rush of wind sends "
      "a chill down your spine.\nAppearing over you in a green mist, a ghost of rotting flesh and bone screams. "
      "“HeLp Me. HELP ME!”  What do you do?\n\n",
"B5b":"You bang on the door again.  This time, the door opens slowly.\nYou see an old man dead on the floor, pie "
      "coming out of his mouth.\n “Murderer!” comes a shout from behind you.  It’s the shady hooded figure from "
      "the Inn.\n“I seen it with my own eyes!”\nAn angry mob begins to descend upon you. You panic, quickly stumble "
      "out of the way, and scrap your\nknees as you pick yourself up and run.  You do not have time to think of where "
      "you are heading, but you run as hard as you can, not stopping for a second.\nYour eyes get heavy, then "
      "everything goes dark.\nWhen your eyes open, you don’t know how much time has passed or where you are.  "
      "You are no longer in the green fields outside Ultime, quite the opposite in fact.\nYou find yourself amid "
      "structures of stone from a civilisation of past.\nThere are decaying archways and bridges over swamps.  "
      "Houses without walls, and the constant,\nfaintly echoing cries of the lost souls bound to this accursed place.  "
      "A rush of wind sends a chill down your spine.\nAppearing over you in a green mist, a ghost of rotting flesh "
      "and bone screams. “HeLp Me. HELP ME!”\nWhat do you do?\n\n",
"B6":"You peer in through the window.  It is hard to make anything out as the room is dimly lit.\nYou spot "
     "something on the floor.  To your horror, you see an old man lying\nstill in a pool of his own blood.  You "
     "jerk away from the window.\n“What’s this?” comes a voice from behind you.\nThe mysterious hooded figure from "
     "the Inn is standing there, with a mischievous grin.\nA few passers-by slow down and look in "
     "your direction.\n“It seems this outsider has killed the poor hermit!” he shouts to the onlookers. "
     "“Justice must be done.” \n"
     "He flings his dagger, which plants itself firmly into the wall, inches from your face.\nHe lunges for you.  "
     "You panic, quickly stumble out of the way, and scrap your knees as you pick yourself up\nand run.  You do not "
     "have time to think of where you are heading,\nbut you run as hard as you can, not stopping for a second.  Your "
     "eyes get heavy, then everything goes dark.\n " "\nWhen your eyes open, you don’t know how much time has passed or "
     "where you are.\nYou are no longer in the green fields outside Ultime, quite the opposite in fact.  You find "
     "yourself amid structures of stone from a civilisation of past.\nThere are decaying archways and bridges over "
     "swamps.  Houses without walls, and the constant,\nfaintly echoing cries of the lost souls bound to this "
     "accursed place.  A rush of wind sends a chill down your spine.\nAppearing over you in a green mist, a ghost "
     "of rotting flesh and bone screams.\n“HeLp Me. HELP MEEE!” What do you do?\n\n",
"B6a":"You scramble around for something to fight off the ghost with.\nYou grab a large stone by your foot "
      "and through it as hard as you can.\nThe ghost looks at you in disbelief as the rock completely passes "
      "through it.\n“Really? Of all the things, you thought that would be a good idea? I may be dead but you’re "
      "the one with dirt for brains.\nThis is why I bloody hate the living; you ask for help but all they know "
      "how to do is resort to violence.”\nThe ghost disappears into the mist, leaving you lost and alone.  "
      "You walk on for hours but it is no good, you are just going around in circles.\nYou give up, falling "
      "to the floor exhausted, waiting for the inevitable end.\nGame over.\n\n",
"B6b":"“Heart… I have lost… my heart… red… shiny.”\nYou show that you are in no possession of such a thing, "
      "much to the dismay of the ghost.\n“Well fiddlesticks. I don’t know where I lost it, but my search "
      "continues.\nWhat’s that? You, like my heart, are lost too? You shouldn’t be\nwondering these woods, "
      "get too deep and you’ll never make it back out.\nListen, just head straight for that large rock in "
      "the distance,\nthen make a right and you’ll come across an old, marooned ship.\nHead in through the hull "
      "and you’ll be out of here.”\n\nListening to the ghost’s directions, you find yourself outside the very ship "
      "he mentioned.  Lucky for you he was telling the truth!\nYou run inside through a gaping hole in the hull. "
      "You stand amazed as the interior looks\nnothing like a decrepit ship. Rows of food-stuffed tables are laid "
      "out, separated by royal red carpets.\nCandles are placed everywhere, even on top of other candles,\nall "
      "melting as one. And ghosts.  A lot more ghosts.\nBut these were not human.  They were sharks, all "
      "dressed smartly in old-fashioned suits.\n“You there!” shouts the largest of them, who happened to be "
      "sitting on a golden throne in the back.\n\n“You finally made it" " " + name + " "",wonderful! You’re probably "
                                                                               "wondering just what in Davy "
                                                                               "Jones’ Locker is going on here.\n"
                                                                               "Just bear in mind, I’m only the "
                                                                               "messenger, but I have direct contact "
                                                                               "with the… shall we say, author, of "
                                                                               "all this.\nYou see, you’re in a game. "
                                                                               "An insultingly simplistic game that "
                                                                               "needs to come to an\nend now before "
                                                                               "those nested if statements become "
                                                                               "too burdensome.\nI don’t know what "
                                                                               "that means either, I’m just telling "
                                                                               "you what I’ve been told.\nLuckily I "
                                                                               "can summon a portal home for you "
                                                                               "because magic.\nStep into the portal "
                                                                               "and you’ve won the game!“\n\n",
"B6c":"“Heart… I have lost… my heart… red… shiny.”\nYou show the glowing red gem you found earlier.\n“MY HEART! Where "
      "did you find it? Please, return it me!”\nYou hand over the heart. The ghost flies up and down in joy before "
      "composing himself.\n“Thank you so much! I always thought the living were insufferable jerks, but you’re "
      "alright.\nWhat’s that? You need to find the way out? \nJust head straight for that large rock in "
      "the distance,\nthen make a right and you’ll come across an old, marooned ship.  Head in through the hull "
      "and you’ll be out of here.”\n\nListening to the ghost’s directions, you find yourself outside the very ship\n "
      "he mentioned.  Lucky for you he was telling the truth!\nYou run inside through a gaping hole in the hull. "
      "You stand amazed as the\ninterior looks nothing like a decrepit ship.\nRows of food-stuffed tables are laid "
      "out, separated by royal red carpets.\nCandles are placed everywhere, even on top of other candles, all\n"
      "melting as one. And ghosts.  A lot more ghosts. But these were not human.\nThey were sharks, all "
      "dressed smartly in old-fashioned suits.\n“You there!” shouts the largest of them, who happened to be\n "
      "sitting on a golden throne in the back.\n\n“You finally made it"" " + name + " "",wonderful! You’re probably "
                                                                               "wondering just what in Davy "
                                                                               "Jones’ Locker is going on here.\n"
                                                                               "Just bear in mind, I’m only the "
                                                                               "messenger, but I have direct contact "
                                                                               "with the… shall we say, author, of "
                                                                               "all this.\nYou see, you’re in a game. "
                                                                               "An insultingly simplistic game that "
                                                                               "needs to come to an\nend now before "
                                                                               "those nested if statements become "
                                                                               "too burdensome.\nI don’t know what "
                                                                               "that means either, I’m just telling "
                                                                               "you what I’ve been told.\nLuckily I "
                                                                               "can summon a portal home for you "
                                                                               "because magic.\nStep into the portal "
                                                                               "and you’ve won the game!“\n\n",
}
def ending():
    """All ending outcomes are within this function"""
    if gem != 0 and map != 0:
        print(
            "Well done! You got the best ending!\n"
            "The lady from Crows Inn and the ghost with his heart are both\n"
            "standing next to the Shark King, waving you good-bye.")
        time.sleep(1.5)
        print("You've earned a pack containing 10 cards!")
        time.sleep(1.5)
        ten_pack()
        input("\nPress any key to return to the main menu.")
        time.sleep(1.5)
        main_menu()
    elif gem != 0 and map == 0:
        print(
            "Well done! You didn't get the best ending, but that's fine!\n"
            "The ghost with his heart is standing next to the Shark King, waving you good-bye.")
        input("\nPress any key to return to the main menu.")
        time.sleep(1.5)
        main_menu()
    elif gem == 0 and map != 0:
        print(
            "Well done! You didn't get the best ending, but that's fine!\n"
            "The lady from Crows Inn is standing next to the Shark King, waving you good-bye.")
        input("\nPress any key to return to the main menu.")
        time.sleep(1.5)
        main_menu()
    else:
        print("Well, you got to the end,\n"
              "but I don't know if I'd call that winning, really. Try again for a better outcome?")
        input("\nPress any key to return to the main menu.")
        time.sleep(1.5)
        main_menu()

# Items
gem = 0
map = 0


###############################################################


#################### M A I N    G A M E #######################


def main_game():
    global name, gem, map
    print(storychoices["B1"])

    choice = input("1) Run toward town\n2) Inspect the bush\n\n")

    if choice == "1":
        print(storychoices["B2"])
        choice = input("1) Fortune Tellers straight ahead\n2) Town exit to the left\n3) Dark Crow Inn to the right\n\n")
        if choice == "1":
            print(storychoices["B2a"])
            choice = input("1) I thought you knew all?\n2) I want to go home\n")
            if choice == "1":
                print(storychoices["B2aa"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            elif choice == "2":
                print(storychoices["B2ab"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            else:
                pass
        elif choice == "2":
            print(storychoices["B2c"])
            choice = input("1) Take parcel\n2) Refuse offer\n\n")
            if choice == "1":
                print(storychoices["B5a"])
                choice = input("1) Attack ghost\n2) Help ghost\n\n")
                if choice == "1":
                    print(storychoices["B6a"])
                elif choice == "2":
                    print(storychoices["B6b"])
                    ending()
            elif choice == "2":
                print(storychoices["B4c"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            else:
                pass
        else:
            print(storychoices["B3"])
            choice = input("1)	Where am I?\n2)	Order a drink\n\n")
            if choice == "1":
                print(storychoices["B4"])
                map += 1
                choice = input("1) Visit the hermit\n2) Ignore Nettles advice and head back to the main market\n\n")
                if choice == "1":
                    print(storychoices["B5"])
                    choice = input("1) Knock again, but harder\n2) Peep through the window\n\n")
                    if choice == "1":
                        print(storychoices["B5b"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()
                    elif choice == "2":
                        print(storychoices["B6"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()
                    else:
                        pass
                elif choice == "2":
                    print(storychoices["B4b"])
                    choice = input("1) Take parcel\n2) Refuse offer\n\n")
                    if choice == "1":
                        print(storychoices["B5a"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()

                    elif choice == "2":
                        print(storychoices["B4c"])
                        input("\nPress any key to return to the main menu.")
                        print(" Very well.")
                        time.sleep(1.5)
                        main_menu()
                    else:
                        pass
                else:
                    pass
            elif choice == "2":
                print(storychoices["B3b"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            else:
                pass
    elif choice == "2":
        print(storychoices["B1b"])
        gem += 1
        print(storychoices["B2"])
        choice = input("1) Fortune Tellers straight ahead\n2) Town exit to the left\n3) Dark Crow Inn to the right\n\n")
        if choice == "1":
            print(storychoices["B2a"])
            choice = input("1) I thought you knew all?\n2) I want to go home\n\n")
            if choice == "1":
                print(storychoices["B2aa"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            elif choice == "2":
                print(storychoices["B2ab"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            else:
                pass
        elif choice == "2":
            print(storychoices["B2c"])
            choice = input("1) Take parcel\n2) Refuse offer\n\n")
            if choice == "1":
                print(storychoices["B5a"])
                choice = input("1) Attack ghost\n2) Help ghost\n\n")
                if choice == "1":
                    print(storychoices["B6a"])
                    input("\nPress any key to return to the main menu.")
                    print(" Very well.")
                    time.sleep(1.5)
                    main_menu()
                elif choice == "2" and gem == 1:
                    print(storychoices["B6c"])
                    ending()
                elif choice == "2":
                    print(storychoices["B6b"])
                    ending()
            elif choice == "2":
                print(storychoices["B4c"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            else:
                pass
        else:
            print(storychoices["B3"])
            choice = input("1)	Where am I?\n2)	Order a drink\n\n")
            if choice == "2":
                print(storychoices["B3b"])
                input("\nPress any key to return to the main menu.")
                print(" Very well.")
                time.sleep(1.5)
                main_menu()
            elif choice == "1":
                print(storychoices["B4"])
                map += 1
                choice = input("1) Visit the hermit\n2) Ignore Nettles advice and head back to the main market\n\n")
                if choice == "1":
                    print(storychoices["B5"])
                    choice = input("1) Knock again, but harder\n2) Peep through the window\n\n")
                    if choice == "1":
                        print(storychoices["B5b"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2" and gem == 1:
                            print(storychoices["B6c"])
                            ending()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()
                    elif choice == "2":
                        print(storychoices["B6"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2" and gem == 1:
                            print(storychoices["B6c"])
                            ending()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()
                    else:
                        pass
                elif choice == "2":
                    print(storychoices["B4b"])
                    choice = input("1) Take parcel\n2) Refuse offer\n\n")
                    if choice == "1":
                        print(storychoices["B5a"])
                        choice = input("1) Attack ghost\n2) Help ghost\n\n")
                        if choice == "1":
                            print(storychoices["B6a"])
                            input("\nPress any key to return to the main menu.")
                            print(" Very well.")
                            time.sleep(1.5)
                            main_menu()
                        elif choice == "2" and gem == 1:
                            print(storychoices["B6c"])
                            ending()
                        elif choice == "2":
                            print(storychoices["B6b"])
                            ending()

                    elif choice == "2":
                        print(storychoices["B4c"])
                        input("\nPress any key to return to the main menu.")
                        print(" Very well.")
                        time.sleep(1.5)
                        main_menu()
                    else:
                        pass
                else:
                    pass
    else:
        pass
    # card_unlock(c1)
    # card_unlock(c2)
    # card_unlock(c3)
    # card_unlock(c4)
    # card_unlock(c5)
    # card_unlock(c6)
    # card_unlock(c7)
    # card_unlock(c8)
    # card_unlock(c9)
    # card_unlock(c10)
    # card_unlock(c11)
    # card_unlock(c12)
    # card_unlock(c13)
    # card_unlock(c14)
    # card_unlock(c15)
    # card_unlock(c16)
    # card_unlock(c17)
    # card_unlock(c18)
    # card_unlock(c19)
    # card_unlock(c20)
    # card_unlock(c21)
    # card_unlock(c22)
    # card_unlock(c23)
    # card_unlock(c24)
    # card_unlock(c25)
    # card_unlock(c26)
    # card_unlock(c27)
    # card_unlock(c28)
    # card_unlock(c29)
    # card_unlock(c30)
    # card_unlock(c31)
    # card_unlock(c32)
    # card_unlock(c33)
    # card_unlock(c34)
    # card_unlock(c35)
    # card_unlock(c36)
    # card_unlock(c37)
    # card_unlock(c38)
    # card_unlock(c39)
    # card_unlock(c40)
    # card_unlock(c41)
    # card_unlock(c42)
    # card_unlock(c43)
    # card_unlock(c44)
    # card_unlock(c45)
    # card_unlock(c46)
    # card_unlock(c47)
    # card_unlock(c48)
    # card_unlock(c49)
    # card_unlock(c50)
    # card_unlock(c51)
    # print("\n\n\n")
    # time.sleep(0.5)
    # print(" A stack of magical cards lay before you on the table. "
    #       "Pick a card from the top and see what you get!")
    # time.sleep(0.5)
    #
    # input(" Press any key to pick a card\n")
    # time.sleep(0.5)
    #
    # result = random.choice(cards)
    # card_unlock(result)
    #
    # input(" Press any key to draw a guaranteed Mythic card! \n")
    # mythic()
    # time.sleep(0.5)
    #
    # input(" Press any key to draw a guaranteed Mythic card! \n")
    # mythic()
    # time.sleep(0.5)
    #
    # print(" Time to try another test.\n")
    # time.sleep(0.5)
    #
    # five_pack()
    #
    # ten_pack()
    # print(" Total Gold: " + str(gold))
    # print(" Fantastic! It all worked as it should. Enjoy your new card collection!\n")
    # time.sleep(0.5)

    option = input(" Would you like to have a look at your card collection?(y/n) ")
    if option == "y" or option == "Y":
        card_album()

    else:
        print(" Very well.")
        time.sleep(1.5)
        main_menu()


####################### G A M E    S T A R T #######################


main_menu()
main_game()


