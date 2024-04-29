#version 1.5
#refinning of the program, bug fixes and making the whole thing just look nicer to a user.
#Also includes the deletion of uneeded code.
import copy
global count
Score = 0
count = 0
exampleboard=[[" "," "," "],
              [" "," "," "],
              [" "," "," "]]
Done = False

#allows the first player to make a move, who is X
def player1(Board,Turn):
    Row = 0
    Col = 0
    while Row != "0" and Row != "1" and Row != "2":
        Row = input("Please select the column (0,1,2)")
    while Col != "0" and Col != "1" and Col != "2": 
        Col = input("Please select the row (0,1,2)")
    Row = int(Row)
    Col = int(Col)
    if Board[Col][Row] == " ":
        Board[Col][Row] = Turn
        return Board
    else:
        print("this space is already occupied")
        player1(Board,Turn)
        return Board
        
def IsDone(Board):
        isDone=False
        #code to check to see if the board is in an endstate.
        for n in range(len(Board)):
        #row wins
            if Board[n][0] == Board[n][1] == Board[n][2]:
                if Board[n][0] == " ":
                    pass
                else:
                    print(Board[n][0], "wins")
                    #calls calculate score with the winner being given as a parameter.
                    isDone = True 
                    return isDone
            #column wins
            if Board[0][n] == Board[1][n] == Board[2][n]:
                if Board[0][n] == " ":
                    pass
                else:
                    print(Board[0][n], "wins")
                    #calls calculate score with the winner being given as a parameter.
                    isDone = True 
                    return isDone 
            #diagonal wins
            if Board[0][0] == Board[1][1] == Board[2][2]:
                if Board[0][0] == " ":
                    pass
                else:
                    print(Board[0][0], "Wins")
                    #calls calculate score with the winner being given as a parameter.
                    isDone = True 
                    return isDone 
            if Board[2][0] == Board[1][1] == Board[0][2]:
                if Board[2][0] == " ":
                    pass
                else:
                    print(Board[2][0], "Wins")
                    #calls calculate score with the winner being given as a parameter.
                    isDone = True 
                    return isDone
        #code to check if the board is full, which is a possible end-state, this only runs once all other win checks have been performed.
        OccupiedSquares = 0
        for n in range(len(Board)):
            for m in range(len(Board[n])):
                if Board[n][m]==" ":
                    pass
                else:
                    OccupiedSquares = OccupiedSquares + 1
                if OccupiedSquares == 9:
                    isDone = True
        return isDone



#The actual MinMax program.
class BoardMinMax:
    #the initial constructor, which is used to create a graph of the possible moves.
    #isRoot is used to check if the node being created is the root node, which the first one always will be.
    #this is needed as the root node cannot have an assigned score,
    #It instead needs to know what the scores of its direct children are and which is the biggest.
    def __init__(self, boardpos, isO,NewScore, isRoot):
        #Creates a 2d array that represents the board,
        self.boardPosition=[[" "," "," "],[" "," "," "],[" "," "," "]]
        #The score given to the particular node.
        if isRoot==True:
            self.Score=None 
        else:
            self.Score = NewScore
        #Variable checking to see if the current board is in an endstate.
        self.EndState=False
        #a list of all direct children nodes of this node.
        self.children=[]
        #checks to see if the node is the root node.
        self.IsRoot=isRoot
        #Makes it so that only the first node created when the board is first initialised is treated as the root node.
        isRoot = False
        #checks who"s turn it is.
        self.NextisO=isO
        #Makes the board equal to the current board position in play in the actual game. 
        self.boardPosition=boardpos
        #determine if in endState.  If is then stop
        #print(self.Score)
        if self.IsEndState() == True:
            pass
                
        else:
        #if the board is not in an endstate, then it generates the children of that board.
            self.GenerateChildren()
            #if the board is not the root, then it creates its score based off of the scores of its children.
            #This is only calculated after all children are created. 
            if self.IsRoot == False:
                #if the player is the minimising, takes the lowest score of the children nodes
                #if maximising, instead takes the highest score.
                self.Score = self.children[0].Score
                for n in range(len(self.children)):
                    if isO == False:
                        if self.children[n].Score > self.Score:
                            self.Score=self.children[n].Score
                        else:
                            pass
                    else:
                        if self.children[n].Score < self.Score:
                            self.Score=self.children[n].Score
                        else:
                            pass
            #if it is the root, the score is given a null value. 
            else:
                self.Score=None
        return
    
    def GenerateChildren(self):
        #code to build all possible child boards
        #all positions on the board are checked to see if they have an empty square.
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m]==" ":
                    #deep copy of board
                    newBoardPos=copy.deepcopy(self.boardPosition)   #this is the deepcopy
                    #if NextisO is true and the square is empty, this is made equal to O
                    if self.NextisO:
                        newBoardPos[n][m]="O"
                    #otherwise it is made equal to X.
                    else:
                        newBoardPos[n][m]="X"
                    #Creates a new board using the MinMax constructor as according to the new board position.
                    #while doing so it flips the turns.
                    newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False)
                    #adds the newly created board to the children boards list. 
                    self.children.append(newBoard)


    def CalcWinner(self,winner):
        #exam board position and return 1 = AI win, -1 Player win, 0 no winner
        if winner == "X":
            outcome = 1
        elif winner == "O":
            outcome = -1
        else:
            outcome=0
        
        return outcome

    def IsEndState(self):
        isDone=False
        #code to check to see if the board is in an endstate.
        for n in range(len(self.boardPosition)):
        #row wins
            if self.boardPosition[n][0] == self.boardPosition[n][1] == self.boardPosition[n][2]:
                if self.boardPosition[n][0] == " ":
                    pass
                else:
                    #calls calculate score with the winner being given as a parameter.
                    winner = self.boardPosition[n][0]
                    self.Score = self.CalcWinner(winner)
                    isDone = True 
                    return isDone
            #column wins
            if self.boardPosition[0][n] == self.boardPosition[1][n] == self.boardPosition[2][n]:
                if self.boardPosition[0][n] == " ":
                    pass
                else:
                    #calls calculate score with the winner being given as a parameter.
                    winner = self.boardPosition[0][n]
                    self.Score = self.CalcWinner(winner)
                    isDone = True 
                    return isDone 
            #diagonal wins
            if self.boardPosition[0][0] == self.boardPosition[1][1] == self.boardPosition[2][2]:
                if self.boardPosition[0][0] == " ":
                    pass
                else:
                    #calls calculate score with the winner being given as a parameter.
                    winner = self.boardPosition[0][0]
                    self.Score = self.CalcWinner(winner)
                    isDone = True 
                    return isDone 
            if self.boardPosition[2][0] == self.boardPosition[1][1] == self.boardPosition[0][2]:
                if self.boardPosition[2][0] == " ":
                    pass
                else:
                    #calls calculate score with the winner being given as a parameter.
                    winner = self.boardPosition[2][0]
                    self.Score = self.CalcWinner(winner)
                    isDone = True 
                    return isDone
        #code to check if the board is full, which is a possible end-state. This only runs once all other possible win checks have been performed.
        OccupiedSquares = 0
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m]==" ":
                    pass
                else:
                    OccupiedSquares = OccupiedSquares + 1
                if OccupiedSquares == 9:
                    #if the board is full, the winner is assigned to be ""
                    winner = ""
                    self.Score = self.CalcWinner(winner)
                    isDone = True
                    return isDone
                else:
                    pass

        return isDone
#main
    #decides if the ai or player goes first.
    #player going first.
    
print("Welcome to the MinMax Noughts and Crosses Program")
print("this was made to try and figure out how to program a MinMax program")
print("to play you have to first pick if you want yourself, or the computer to go first")
print("Then when it is your turn, you have to select which column you want to make a move in, then which row you want to make a move in")
print("The rows and columns start from 0, so the first row is row 0")
print("The computer will then make a move, and then it will be your turn again")
print("======================================================================")
First = 0
while First != "1" and First != "2":
    print("Do you want the computer to go first or second ? (1 for first, 2 for second)")
    First = input(">")
if First == "2":
    Turn = "O"
    while Done == False:
        #player1 turn
        exampleboard = player1(exampleboard,Turn)
        #checks if the board is in an endstate
        for n in range(len(exampleboard)):
            print(exampleboard[n])
        Done = IsDone(exampleboard)
        if Done == True:
            break
    #The second parameter should be set to False, determines who goes first. True is O, False is X
        #the ai turn
        board1=BoardMinMax(exampleboard,False, Score, True)
    #this sets the highest score of the children nodes of the root nodes to be the first node, which it may not be, but this is required.
        HighScore = board1.children[0].Score
    #this sets the position in the list of children nodes to contain the node with the highest score to be 0, the first location. 
        HighScorePos = 0
        for n in range(len(board1.children)):
            print(board1.children[n].Score)
            print(board1.children[n].boardPosition)
        #this changes the highscore if the score found for a different child node is greater, if it is less or equals to it does not change.
            if board1.children[n].Score > HighScore:
                HighScore = board1.children[n].Score
            #this tells were in the children list the highscore has been found.
                HighScorePos = n

        HighscoreBoard = copy.deepcopy(board1.children[HighScorePos].boardPosition)
    #should run three times
        for n in range(len(exampleboard)):
        #should run three times, so the whole loop should run 9 times total
            #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
            #it finds the difference and returns the x y coordinates of this difference.
            for m in range(0,3):
                if exampleboard[n][m] != HighscoreBoard[n][m]:
                    y = n
                    x = m
        exampleboard[y][x] = "X"
        Done = IsDone(exampleboard)
        print("==========================")
        for n in range(len(exampleboard)):
            print(exampleboard[n])
        if Done == True:
            break
    #ai going first.
elif First == "1":
    print("This may take some time")
    Turn = "O"
    while Done == False:
    #The second parameter should be set to False, determines who goes first. True is O, False is X
        #the ai turn
        board1=BoardMinMax(exampleboard,False, Score, True)
    #this sets the highest score of the children nodes of the root nodes to be the first node, which it may not be, but this is required.
        HighScore = board1.children[0].Score
    #this sets the position in the list of children nodes to contain the node with the highest score to be 0, the first location. 
        HighScorePos = 0
        for n in range(len(board1.children)):
            print(board1.children[n].Score)
            print(board1.children[n].boardPosition)
        #this changes the highscore if the score found for a different child node is greater, if it is less or equals to it does not change.
            if board1.children[n].Score > HighScore:
                HighScore = board1.children[n].Score
            #this tells were in the children list the highscore has been found.
                HighScorePos = n
        HighscoreBoard = copy.deepcopy(board1.children[HighScorePos].boardPosition)
    #should run three times
        for n in range(len(exampleboard)):
        #should run three times, so the whole loop should run 9 times total
            #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
            #it finds the difference and returns the x y coordinates of this difference.
            for m in range(0,3):
                if exampleboard[n][m] != HighscoreBoard[n][m]:
                    y = n
                    x = m
        exampleboard[y][x] = "X"
        Done = IsDone(exampleboard)
        print("=========================")
        for n in range(len(exampleboard)):
            print(exampleboard[n])
        if Done == True:
            break
        #player1 turn
        exampleboard = player1(exampleboard,Turn)
        #checks if the board is in an endstate
        for n in range(len(exampleboard)):
            print(exampleboard[n])
        Done = IsDone(exampleboard)
        if Done == True:
            break
    else:
            pass
         
