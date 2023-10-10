#Create a database to keep track of random monsters in a game Use the existing template as a guide and populate a list:

#Rules:

#each primary stat is generated as 3 random dice rolls (random 1-6) (strength, intelligance, piety, agility, stamina, charm)
#distribution of level is 1: 40%, 2: 30%, 3: 20%, 4: 10%
#each npc gets random 1-10 hp per level
#each npc gets some random money
#30% chance to have 0-6 gold
#50% chance go have 3-12 silver
#if they had no gold, they have a 75% chance to have 4-20 copper
#each gold is worth 10 silver and each silver is worth 10 copper
#Create 100 NPC's Generate a report that shows the distribution of NPC's by level Generatea a report that shows the 
# mean and standard deviation for the following:

#HP
#Wealth (in copper. For example 2 gold, 3 silver and 4 copper has a wealth of 234)

import random
from task2 import mean 


class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    #print(stats)
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        self.stats =  { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
        self.levelup()
        pass
    def traits(self):
        attributes = ("strength","intelligence","piety","agility","stamina","charm")        
        for e in self.stats:
            for i in range(3):
                self.stats[e] += random.randint(1,6)
        return self.stats
    
    def levelup(self):
        leveldistribution = ['1'] *40 + ['2'] * 30 + ['3'] * 20 + ['4'] * 10
        levelselected = random.choice(leveldistribution)
        self.levelhealth = int(levelselected)
        return levelselected
    
    def raisedhp(self):
        addedhp = 0
        for i in range(self.levelhealth):
            healthy = random.randint(1,10)
            addedhp += healthy
        return addedhp

    def wealth(self):
        chance = random.randint(1,10)
        if chance <= 3:
            gold = random.randint(0,6)
        else:
            gold = 0
        chance = random.randint(1,10)
        if chance <= 5:
            silver = random.randint(3,12)
        else:
            silver = 0
        if gold == 0:
            chance = random.randint(1,100)
            if chance <= 75:
                copper = random.randint(4,20)
            else:
                copper = 0
        else:
            copper = 0
        self.g = gold
        self.s = silver
        self.c = copper 
        return ((gold* 100) + (silver *10) + copper)
hplist=[]
wlist = []
for i in range(100):
    y = NPC()
    stats = y.traits()
    #print(stats)
    level = y.levelup()
    #print(level)
    hp = y.raisedhp()
    #print(hp)
    hplist.append(hp)
    mobtotalwealth = y.wealth()
    wlist.append(mobtotalwealth)
    print(mobtotalwealth)
    y = None
    
sumtotalwealth = sum(wlist)
totalhealth = sum(hplist)

meanhealth = (totalhealth/100)

healthdeviant = [(i - meanhealth)**2 for i in hplist]
hpvariant = sum(healthdeviant)/100
hpvariable = (hpvariant**0.5)

print(f"the mean health is: {meanhealth}, and the deviant is: {round(hpvariable,2)}")

meantotalwealth = (sumtotalwealth/100)

wealthdeviant = [(i - meantotalwealth)**2 for i in wlist]
wvariant = sum(wealthdeviant)/100
wvariable = (wvariant ** 0.5)

print(f"the mean wealth is: {meantotalwealth}, and the deviant is: {round(wvariable,2)}")




    


    