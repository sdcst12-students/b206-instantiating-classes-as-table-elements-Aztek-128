from typing import AnyStr


class team:
    wins = 0
    losses = 0
    games = 0
    results = {}

    def points(self, points):        
        recordData[self.name]["Points"] +=points
        
    
    #def record(self, records):
        #if self.name 
        #return

    def win(self, wins):
        if wins["s1"] > wins["s2"]:
            recordData[self.name]["Wins"] +=1
        else:
            pass
        
    
    def loss(self, losses):
        if losses["s1"] < losses["s2"]:
            recordData[self.name]["Losses"] +=1
        elif losses["s1"] == losses["s2"]:
            recordData[self.name]["Ties"] +=1
        
    
    def __init__(self, teammate):
        self.name = teammate
        recordData[self.name]["GamesPlayed"]+=1

        
Players = ["A","B","C","D","E","F","G"]
gameData = [{'t1': 'A', 's1': 2, 't2': 'B', 's2': 3}, {'t1': 'A', 's1': 4, 't2': 'C', 's2': 3}, {'t1': 'A', 's1': 1, 't2': 'D', 's2': 0}, {'t1': 'A', 's1': 0, 't2': 'E', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'F', 's2': 2}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'B', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'C', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 0}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 1}, {'t1': 'B', 's1': 2, 't2': 'G', 's2': 0}, {'t1': 'C', 's1': 0, 't2': 'A', 's2': 2}, {'t1': 'C', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'C', 's1': 3, 't2': 'D', 's2': 4}, {'t1': 'C', 's1': 1, 't2': 'E', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'F', 's2': 4}, {'t1': 'C', 's1': 3, 't2': 'G', 's2': 1}, {'t1': 'D', 's1': 1, 't2': 'A', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'B', 's2': 0}, {'t1': 'D', 's1': 4, 't2': 'C', 's2': 4}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 3}, {'t1': 'D', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 2, 't2': 'A', 's2': 0}, {'t1': 'E', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 2}, {'t1': 'E', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'E', 's1': 0, 't2': 'F', 's2': 4}, {'t1': 'E', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'A', 's2': 1}, {'t1': 'F', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'C', 's2': 4}, {'t1': 'F', 's1': 0, 't2': 'D', 's2': 1}, {'t1': 'F', 's1': 0, 't2': 'E', 's2': 1}, {'t1': 'F', 's1': 2, 't2': 'G', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'A', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'G', 's1': 0, 't2': 'D', 's2': 3}, {'t1': 'G', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'G', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'G', 's1': 2, 't2': 'F', 's2': 3}, {'t1': 'G', 's1': 2, 't2': 'E', 's2': 2}, {'t1': 'G', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'G', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'G', 's1': 0, 't2': 'B', 's2': 0}, {'t1': 'G', 's1': 0, 't2': 'A', 's2': 0}, {'t1': 'F', 's1': 1, 't2': 'G', 's2': 4}, {'t1': 'F', 's1': 2, 't2': 'E', 's2': 3}, {'t1': 'F', 's1': 1, 't2': 'D', 's2': 3}, {'t1': 'F', 's1': 0, 't2': 'C', 's2': 1}, {'t1': 'F', 's1': 4, 't2': 'B', 's2': 2}, {'t1': 'F', 's1': 4, 't2': 'A', 's2': 4}, {'t1': 'E', 's1': 4, 't2': 'G', 's2': 1}, {'t1': 'E', 's1': 3, 't2': 'F', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'D', 's2': 0}, {'t1': 'E', 's1': 0, 't2': 'C', 's2': 4}, {'t1': 'E', 's1': 3, 't2': 'B', 's2': 3}, {'t1': 'E', 's1': 4, 't2': 'A', 's2': 0}, {'t1': 'D', 's1': 0, 't2': 'G', 's2': 2}, {'t1': 'D', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'D', 's1': 2, 't2': 'E', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'C', 's2': 3}, {'t1': 'D', 's1': 4, 't2': 'B', 's2': 1}, {'t1': 'D', 's1': 3, 't2': 'A', 's2': 0}, {'t1': 'C', 's1': 2, 't2': 'G', 's2': 1}, {'t1': 'C', 's1': 1, 't2': 'F', 's2': 3}, {'t1': 'C', 's1': 4, 't2': 'E', 's2': 4}, {'t1': 'C', 's1': 4, 't2': 'D', 's2': 3}, {'t1': 'C', 's1': 1, 't2': 'B', 's2': 1}, {'t1': 'C', 's1': 3, 't2': 'A', 's2': 1}, {'t1': 'B', 's1': 3, 't2': 'G', 's2': 3}, {'t1': 'B', 's1': 3, 't2': 'F', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'E', 's2': 2}, {'t1': 'B', 's1': 3, 't2': 'D', 's2': 1}, {'t1': 'B', 's1': 4, 't2': 'C', 's2': 2}, {'t1': 'B', 's1': 0, 't2': 'A', 's2': 1}, {'t1': 'A', 's1': 2, 't2': 'G', 's2': 4}, {'t1': 'A', 's1': 1, 't2': 'F', 's2': 0}, {'t1': 'A', 's1': 4, 't2': 'E', 's2': 3}, {'t1': 'A', 's1': 4, 't2': 'D', 's2': 2}, {'t1': 'A', 's1': 1, 't2': 'C', 's2': 2}, {'t1': 'A', 's1': 4, 't2': 'B', 's2': 0}]
#Ants, Bears, Cougars, Doges, Elephants, Foxes, Giants
recordData = {i : {"Points": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0,"Ties": 0} for i in Players}
#recordData = {"A":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"B":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"C":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"D":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"E":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"F":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0},"G":{"scores": 0,"GamesPlayed": 0,"Wins": 0,"Losses": 0}}

for i in gameData:
    y = team(i["t1"])
    y.points(i["s1"])
    y.win(i)
    y.loss(i)

    y = team(i["t2"])
    y.points(i["s2"])
    y.win(i)
    y.loss(i)

print(recordData)    

'''
Ants
Bears
Cougars
Doges
Elephants
Foxes
Giants
'''