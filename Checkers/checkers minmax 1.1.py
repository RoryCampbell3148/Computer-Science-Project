#version 1.1, attempted to impliment the minmax program from naughts and crosses into the limited checkers.
#the starting board of the game.
import copy
global Counter
Counter = 0
CoOrds = []
Score = 0
Done = False
NumO = 0
NumX = 0
Board = [["","X","","X"],
         ["X","","X",""],
         ["","X","","X"],
         ["","","",""],
         ["","","",""],
         ["O","","O",""],
         ["","O","","O"],
         ["O","","O",""]]


#player1 is O
#this allows the first player to make a move.
def player1(Board):
    Valid = False
    while Valid == False:
    #asks the player to select the column the piece they want to move is on.
        col = int(input("What column is the piece you want to move on (0,3)?"))
    #asks the player what row is your piece on
        row = int(input("What row is the piece you want to move on(0,7)?"))
    #checks that the piece is actually there.
        if Board[row][col] == "O":
            #asks the player if they want to move their piece left or right.
            LorR = input("do you want to move left or right(1 for left, 2 for right) ?")
            #checks to see if the move is actually possible, so if there is something in the way or the edge of the board
            if LorR == "1":
                #checks if the possible move would still be on the board
                if col == 0 or row == 0:
                    print("This is not a valid move")
                else:
                    #checks to see that the piece is not moving into one of its own.
                    if Board[row-1][col-1] != "O":
                        Board[row-1][col-1] = "O"
                        Board[row][col] = ""
                        Valid = True
                        for n in range(len(Board)):
                            print(Board[n])
                    else:
                        print("This is not a valid move")
                        
            elif LorR == "2":
                 #checks if the possible move would still be on the board
                if col == 3 or row == 0:
                    print("This is not a valid move")
                else:
                    #checks to see that the piece is not moving into one of its own.
                    if Board[row-1][col+1] != "O":
                        Board[row-1][col+1] = "O"
                        Board[row][col] = ""
                        Valid = True
                        for n in range(len(Board)):
                            print(Board[n])
                    else:
                        print("This is not a valid move")
                
             
        else:
            Valid = False
            print("There is no piece here")

#player2 is X
#this allows the second player to make a move.
def player2(Board):
    Valid = False
    while Valid == False:
    #asks the player to select the column the piece they want to move is on.
        col = int(input("What column is the piece you want to move on (0,3)?"))
    #asks the player what row is your piece on
        row = int(input("What row is the piece you want to move on(0,7)?"))
    #checks that the piece is actually there.
        if Board[row][col] == "X":
            #asks the player if they want to move their piece left or right.
            LorR = input("do you want to move left or right(1 for left, 2 for right) ?")
            #checks to see if the move is actually possible, so if there is something in the way or the edge of the board
            if LorR == "1":
                #checks if the possible move would still be on the board
                if col == 0 or row == 7:
                    print("This is not a valid move")
                else:
                    #checks to see that the piece is not moving into one of its own.
                    if Board[row+1][col-1] != "X":
                        Board[row+1][col-1] = "X"
                        Board[row][col] = ""
                        Valid = True
                        for n in range(len(Board)):
                            print(Board[n])
                    else:
                        print("This is not a valid move")
                        
            elif LorR == "2":
                 #checks if the possible move would still be on the board
                if col == 3 or row == 7:
                    print("This is not a valid move")
                else:
                    #checks to see that the piece is not moving into one of its own.
                    if Board[row+1][col+1] != "X":
                        Board[row+1][col+1] = "X"
                        Board[row][col] = ""
                        Valid = True
                        for n in range(len(Board)):
                            print(Board[n])
                    else:
                        print("This is not a valid move")
                
             
        else:
            Valid = False
            print("There is no piece here")

#checks to see if one player has won.
def checkwin(Board,NumX,NumO):
    #checks to see if either side still has all their pieces.
    #runs throught the entire board and counts up the total number of X's
    for n in range(len(Board)):
        for m in range(len(Board[n])):
            if Board[n][m] == "X":
                NumX = NumX + 1
                #runs through the entire board and counts up the number of O's
                for n in range(len(Board)):
                    for m in range(len(Board[n])):
                        if Board[n][m] == "O":
                            NumO = NumO + 1
                            #checks to see if either player has reached the end of the board.
                            for n in range(len(Board[0])):
                                if Board[0][n] == "O":
                                    print("O WINS")
                                    return True
                                else:
                                    return False
                            for n in range(len(Board[7])):
                                if Board[7][n] == "X":
                                    print("X WINS")
                                    return True
                                else:
                                    return False
    if NumX == 0:
        print("O WINS")
        return True
    if NumO == 0:
        print("X WINS")
        return True

#finds the best possible move.
def bestMove(board1,Score,HighScore):
    CoOrds = []
    #best variables are to be set to the row and col that the new move is to be made.
    BestRow = 0
    BestCol = 0
    #Old Variables are to be set to the row and col were the piece that was moved used to be.
    OldRow = 0
    OldCol = 0
    #runs for as many times as there are children nodes of the root node.
    for n in range(len(board1)):
        #if the score of one of the children nodes is greater than the current highscore,
        #this board is searched through and the difference between this board and the previous board is found
        if Score > HighScore or Score == HighScore:
            print("===")
            print(Score)
            print(HighScore)
            print("===")
            HighScore = Score
            #print("===")
            #print(HighScore)
            #print("===")
            for n in range(len(Board)):
            #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
            #it finds the difference and returns the x y coordinates of this difference.
                for m in range(len(Board[n])):
                    if Board[n][m] != board1[n][m]:
                        if board1[n][m] == "X":
                            print(n)
                            print(m)
                            BestRow = n
                            BestCol = m
                        elif board1[n][m] == "":
                            print(n)
                            print(m)
                            OldRow = n
                            OldCol = m

    CoOrds = [BestRow,BestCol,OldRow,OldCol]
    return CoOrds
    
    
    
    

    
#The actual MinMax program.
class BoardMinMax:
    #the initial constructor, which is used to create a graph of the possible moves.
    #isRoot is used to check if the node being created is the root node, which the first one always will be.
    #this is needed as the root node cannot have an assigned score,
    #It instead needs to know what the scores of its direct children are and which is the biggest.
    def __init__(self, boardpos, isO,NewScore, isRoot):
        #Creates a 2d array that represents the board,
        self.boardPosition=[["","X","","X"],
                            ["X","","X",""],
                            ["","X","","X"],
                            ["","","",""],
                            ["","","",""],
                            ["O","","O",""],
                            ["","O","","O"],
                            ["O","","O",""]]
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
        global Counter
        Counter = Counter + 1
        if self.IsRoot == True:
            print(Counter)
        #print(self.Score)
        #print("======================================================")
        #for n in range(len(self.boardPosition)):
        #    print(self.boardPosition[n])
        #print("======================================================")
        if self.Score != 0:
            print(self.Score)
        if self.IsEndState() == True:
        #    global count  
        #    count = count + 1
        #    if count == 255168:
        #        print(count)
        #    elif count > 255168:
        #        print(count)
        #    else:
            pass
                
        else:
        #if the board is not in an endstate, then it generates the children of that board.
            #(self.boardPosition)
            self.GenerateChildren()
            #if the board is not the root, then it creates its score based off of the scores of its children.
            #This is only calculated after all children are created. 
            if self.IsRoot == False:
                #if the player is the minimising, takes the lowest score of the children nodes
                #if maximising, instead takes the highest score.
                for n in range(len(self.children)):
                    if isO == False:
                        #print("=============")
                        #print(self.children[n].Score)
                        if self.children[n].Score > 0:
                            self.Score=self.children[n].Score
                           # print(self.Score)
                           # print("=============")
                        else:
                            self.Score = self.children[n].Score
                    else:
                        if self.children[n].Score < 0:
                            self.Score=self.children[n].Score
                        else:
                            self.Score=self.children[n].Score
            #if it is the root, the score is given a null value. 
            else:
                self.Score=None
        return
    
    #test method to add a child board
    #creates a new child board according to the current board position.
    def AddChild(self, boardpos):
        #create a new board out of the minmax constructor.
        #not self.NextisO is used to flip the turn.
        newBoard=BoardMinMax(boardpos,not self.NextisO)
        #adds the new board to the list of children boards.
        self.children.append(newBoard)
        print(self.children)
        return
    
    def GenerateChildren(self):
        #code to build all possible child boards
        #all positions on the board are checked to see if they have an empty square.
        for row in range(len(self.boardPosition)):
            for col in range(len(self.boardPosition[row])):
                #runs if it is O's turn.
                if self.NextisO:
                    if self.boardPosition[row][col] == "O":
                    #If the computer is able to go both left and right, it will first go left and go down that tree,
                    #it will then backtrack back and go right and go down that tree.
                    #checks to see if the computer is able to make a valid move. In this case going left
                        if col == 0 or row == 0:
                            pass
                    #if the computer can make the move, it does. If it doesn't it passes as shown above.
                        else:
                    #checks to see that the piece is not moving into one of its own.
                            if Board[row-1][col-1] != "O":
                                #deep copy of board
                                newBoardPos=copy.deepcopy(self.boardPosition)   #this is the deepcopy
                                newBoardPos[row-1][col-1] = "O"
                                newBoardPos[row][col] = ""
                                #Creates a new board using the MinMax constructor as according to the new board position.
                            #while doing so it flips the turns.
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                            else:
                                pass
                        #this is going right.
                        if col == 3 or row == 0:
                            pass
                        else:
                        #checks to see that the piece is not moving into one of its own.
                            if Board[row-1][col+1] != "O":
                                #deep copy of board
                                newBoardPos=copy.deepcopy(self.boardPosition)   #this is the deepcopy
                                newBoardPos[row-1][col+1] = "O"
                                newBoardPos[row][col] = ""
                                #Creates a new board using the MinMax constructor as according to the new board position.
                            #while doing so it flips the turns.
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                            else:
                                pass
                #if it is X's turn
                else:
                    if self.boardPosition[row][col] =="X":
                    #If the computer is able to go both left and right, it will first go left and go down that tree,
                    #it will then backtrack back and go right and go down that tree.
                    #checks to see if the computer is able to make a valid move. In this case going left
                        if col == 0 or row == 7:
                            pass
                    #if the computer can make the move, it does. If it doesn't it passes as shown above.
                        else:
                    #checks to see that the piece is not moving into one of its own.
                            if Board[row+1][col-1] != "X":
                                #deep copy of board
                                newBoardPos=copy.deepcopy(self.boardPosition)   #this is the deepcopy
                                newBoardPos[row+1][col-1] = "X"
                                newBoardPos[row][col] = ""
                                #Creates a new board using the MinMax constructor as according to the new board position.
                            #while doing so it flips the turns.
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                            #for n in range(len(Board)):
                            #    print(Board[n])
                            else:
                                pass
                        #this is going right.
                        if col == 3 or row == 7:
                            pass
                        else:
                        #checks to see that the piece is not moving into one of its own.
                            if Board[row+1][col+1] != "X":
                                #deep copy of board
                                newBoardPos=copy.deepcopy(self.boardPosition)   #this is the deepcopy
                                newBoardPos[row+1][col+1] = "X"
                                newBoardPos[row][col] = ""
                                #Creates a new board using the MinMax constructor as according to the new board position.
                            #while doing so it flips the turns.
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                                #for n in range(len(Board)):
                                 #   print(Board[n])
                            else:
                                pass
                    
                    


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
        NumX = 0
        NumO = 0
        isDone=False
            #code to check to see if the board is in an endstate.
            #checks to see if either side still has all their pieces.
        #runs throught the entire board and counts up the total number of X's
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m] == "X":
                    NumX = NumX + 1
                    #runs through the entire board and counts up the number of O's
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m] == "O":
                    NumO = NumO + 1
                    #checks to see if either player has reached the end of the board.
        for n in range(len(self.boardPosition[0])):
            if self.boardPosition[0][n] == "O":
                #print("O WINS")
                winner = "O"
                self.Score = self.CalcWinner(winner)
                isDone = True 
                return isDone
        for n in range(len(self.boardPosition[7])):
            if self.boardPosition[7][n] == "X":
                #print("X WINS")
                winner = "X"
                self.Score = self.CalcWinner(winner)
                #print(self.Score)
                isDone = True 
                return isDone
    #if one side has been anihlated, and has no pieces left on the board, then the other side wins.
        if NumX == 0:
            #print("O WINS")
            winner = "O"
            self.Score = self.CalcWinner(winner)
            isDone = True 
            return isDone
        if NumO == 0:
            #print("X WINS")
            winner = "X"
            self.Score = self.CalcWinner(winner)
            isDone = True 
            return isDone
        


                        
                
#main            
while Done == False:
    for n in range(len(Board)):
        print(Board[n])
    player1(Board)
    Done = checkwin(Board,NumX,NumO)
    if Done == True:
        break
    board1=BoardMinMax(Board,False, Score, True)
    print(Counter)
    Counter = 0
    HighScore = 0
    for n in range(len(board1.children)):
        print(board1.children[n].boardPosition)
        print(board1.children[n].Score)
        CoOrds = bestMove(board1.children[n].boardPosition,board1.children[n].Score,HighScore)
    print(CoOrds)
    BestRow = CoOrds[0]
    BestCol = CoOrds[1]
    OldRow = CoOrds[2]
    OldCol = CoOrds[3]
    Board[BestRow][BestCol] = "X"
    Board[OldRow][OldCol] = ""
    Done = checkwin(Board,NumX,NumO)

