import random
class RPSai:
    def __init__(self):
        self.history = []
        self.rock = 'R'
        self.paper = 'P'
        self.scissors = 'S'
        self.lastMove = ''

    def opponentMove(self,move):
        if move == 'R':
            self.history.append(self.rock)
        elif move == 'P':
            self.history.append(self.paper)
        elif move == 'S':
            self.history.append(self.scissors)
        else:
            print('ERROR')

    def beatMove(self,oppmove):
        if oppmove == 'R':
            return 'P'
        if oppmove == 'P':
            return 'S'
        if oppmove == 'S':
            return 'R'

    def predictMove(self):
        Rcount = 0
        Pcount = 0
        Scount = 0
        for move in self.history:
            if move == 'R':
                Rcount +=1
            if move == 'P':
                Pcount +=1
            if move == 'S':
                Scount +=1
        if Rcount > Pcount and Rcount > Scount:
            return 'R'
        if Scount > Pcount and Scount > Rcount:
            return 'S'
        if Pcount > Rcount and Pcount > Scount:
            return 'P'
        if Pcount == Rcount == Scount:
            return ['R','S','P'][random.randint(0,2)]

    def playMove(self):
        expmove = self.predictMove()
        move = self.beatMove(expmove)
        return move

    def playMovePro(self):
        if len(self.history) < 1:
            move = ['R','S','P'][random.randint(0,2)]
            self.lastMove = move
            return move

        elif (self.history[-1]+self.lastMove) in ["RS","SP","PR"]:
            if self.lastMove == "R":
                self.lastMove = "P"
                return "P"
            if self.lastMove == "P":
                self.lastMove = "S"
                return "S"
            if self.lastMove == "S":
                self.lastMove = "R"
                return "R"

        else:
           move = self.history[-1]
           if move == 'R':
               self.lastMove = "P"
               return 'P'
           elif move == 'P':
               self.lastMove = "S"
               return 'S'
           else:
               self.lastMove = "R"
               return 'R'


