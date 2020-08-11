import random
from asciiplc import intro, dicefunk

class player:
    def __init__(self):
        self.score = 0
        self.dice = [0,0,0,0,0]

    def roll(self):
        for a in range(0,5):
            self.dice[a] = random.randint(1,6)
            dicefunk(self.dice[a])
    
    def upperscore(self, dnum):
        for b in range(0,5):
            if self.dice[b] == dnum: self.score += dnum
        print("Your score is now " + str(self.score))
        rors()

def endgame():
    if p1.score >= 63: print("Congrants you scored over 63 points, that means you get a bonus 35 points!\nChanging your score from " + str(p1.score) + " to " + str(p1.score + 35) + ".")
    else: print("Good game! You scored " + str(p1.score) + " points!")
    intro()

def uord():
    global single
    while True:
        choice = "1"
        choice = input("Would you like to add up 1's, 2's, 3's, 4's, 5's, or 6's?\n7)Finish Game\n")
        if int(choice) == 1 and single[0] == True:
            single[0] = False
            p1.upperscore(int(choice))
        elif int(choice) == 1: print("You have already chosen 1")
        elif int(choice) == 2 and single[1] == True:
            single[1] = False
            p1.upperscore(int(choice))
        elif int(choice) == 2: print("You have already chosen 2")
        elif int(choice) == 3 and single[2] == True:
            single[2] = False
            p1.upperscore(int(choice))
        elif int(choice) == 3: print("You have already chosen 3")
        elif int(choice) == 4 and single[3] == True:
            single[3] = False
            p1.upperscore(int(choice))
        elif int(choice) == 4: print("You have already chosen 4")
        elif int(choice) == 5 and single[4] == True:
            single[4] = False
            p1.upperscore(int(choice))
        elif int(choice) == 5: print("You have already chosen 5")
        elif int(choice) == 6 and single[5] == True:
            single[5] = False
            p1.upperscore(int(choice))
        elif int(choice) == 6: print("You have already chosen 6")
        elif int(choice) == 7:
            endgame()
        else: print("Sorry didn't get that, come again?")

def rors():
    p1.roll()
    rollnum = 1
    while True:
        ragn = input("1)Roll again?\n2)Score\n")
        if int(ragn) == 1 and rollnum < 3: 
            p1.roll()
            rollnum += 1
            print("You have " + str(3-rollnum) + " roll(s) left!")
        elif int(ragn) == 2: uord()
        elif rollnum >= 3:
            print("You ran out of rolls.") 
            rollnum = 1
            uord()
        else: print("Sorry what was that?")

p1 = player()
single = [True,True,True,True,True,True]

def bb():
    froll = input("Would you like to play Yahtzee?(y/n)")
    if froll == "n": print("Welp, too bad. ¯\_(ツ)_/¯")
    elif froll != "y": print("Sorry didn't get that. ASSUMED ANSWER: yes")

    intro()
    print("Here is your fist roll.")
    rors()
bb()