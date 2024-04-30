#Version 1.5. Actual final version, removal of unecessary code and debug code.
#Program no longer crashses.
#Board print out looks nicer.
#inputs are fully sanitised
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
    #asks the player to select the column the piece they want to move is on.
    col = 0
    while col != "0" and col != "1" and col != "2" and col != "3":
        col = input("What column is the piece you want to move on (0,3)?")
    col = int(col)
    #asks the player what row is your piece on
    row = 0
    while row != "0" and row != "1" and row != "2" and row != "3" and row != "4" and row != "5" and row != "6" and row != "7":
        row = input("What row is the piece you want to move on(0,7)?")
    row = int(row)
    #checks that the piece is actually there.
    if Board[row][col] == "O":
                #asks the player if they want to move their piece left or right.
        LorR = 0
        while LorR != "1" and LorR !="2":
            LorR = input("do you want to move left or right(1 for left, 2 for right) ?")
                    #checks to see if the move is actually possible, so if there is something in the way or the edge of the board
        if LorR == "1":
                        #checks if the possible move would still be on the board
            if col == 0 or row == 0:
                print("This is not a valid move")
                player1(Board)
                return Board
            else:
                            #checks to see that the piece is not moving into one of its own.
                if Board[row-1][col-1] != "O":
                    Board[row-1][col-1] = "O"
                    Board[row][col] = ""
                    Valid = True
                    displayboard(Board)
                else:
                    print("This is not a valid move")
                    player1(Board)
                    return Board
                                
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
                    displayboard(Board)
                else:
                    print("This is not a valid move")
                    player1(Board)
                    return Board
                        
                     
    else:
        Valid = False
        print("There is no piece here")
        player1(Board)
        return Board
    return Board


def displayboard(Board):
    print("  | 0 | 1 | 2 | 3 |")
    counter = 0
    for n in range (len(Board)):
        String = ""
        for m in Board[n]:
            if m !="X" and m !="O":
                m = "-"
            String = String + m
            String = String + " | "
        print(counter,"|",String)
        counter = counter + 1
    
    

    
          

#checks to see if one player has won.
def checkwin(Board,NumX,NumO):             
#checks to see if either player has reached the end of the board.
    for n in range(len(Board[0])):
        if Board[0][n] == "O":
            print("O WINS")
            displayboard(Board)
            return True
        else:
            pass
    for n in range(len(Board[7])):
        if Board[7][n] == "X":
            print("X WINS")
            displayboard(Board)
            return True
        else:
            pass
        #checks to see if either side still has all their pieces.
     #runs through the entire board and counts up the number of O's
    for n in range(len(Board)):
        for m in range(len(Board[n])):
            if Board[n][m] == "O":
                NumO = NumO + 1
                
        #runs throught the entire board and counts up the total number of X's
    for n in range(len(Board)):
        for m in range(len(Board[n])):
            if Board[n][m] == "X":
                NumX = NumX + 1
                
    if NumX == 0:
        print("O WINS")
        displayboard(Board)
        return True
    if NumO == 0:
        print("X WINS")
        displayboard(Board)
        return True
    return False

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
            HighScore = Score
            for n in range(len(Board)):
            #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
            #it finds the difference and returns the x y coordinates of this difference.
                for m in range(len(Board[n])):
                    if Board[n][m] != board1[n][m]:
                        if board1[n][m] == "X":
                            BestRow = n
                            BestCol = m
                        elif board1[n][m] == "":
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
    #NumChild is used to check how many children boards there are, it starts at zero with the root board then counts up one every time a child board is created.
    #This is used to prevent the ai going too deep so that there isn't too much time between moves.
    def __init__(self, boardpos, isO,NewScore, isRoot,NumberOfChildren):
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
        #Records how many children there are behind this board, naturally with the root board it starts with zero.
        self.NumChild = NumberOfChildren
        #determine if in endState.  If is then stop
        global Counter
        if self.IsEndState() == True:
            pass
                
        else:
        #if the board is not in an endstate, then it generates the children of that board.
            #if the number of children before it is a set value, then children will not be generated.
            #this is to stop the ai taking too long between turns.
            if self.NumChild < 8:
                self.NumChild = self.NumChild + 1
                self.GenerateChildren()
                #if the board is not the root, then it creates its score based off of the scores of its children.
                #This is only calculated after all children are created. 
                if self.IsRoot == False:
                    #if the player is the minimising, takes the lowest score of the children nodes
                    #if maximising, instead takes the highest score.
                    if len(self.children) > 0:
                        self.Score = self.children[0].Score
                    else:
                        self.Score = 0 
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
            else:
                pass
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
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False,self.NumChild)
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
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False,self.NumChild)
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
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False,self.NumChild)
                            #adds the newly created board to the children boards list.
                                self.children.append(newBoard)
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
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False,self.NumChild)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                            else:
                                pass
                    
                    


    def CalcWinner(self,winner):
        #exam board position and return 1 = AI win, -1 Player win, 0 no winner
        if winner == "X":
            outcome = 10
        elif winner == "O":
            outcome = -10
        else:
            outcome=0
        
        return outcome

    def IsEndState(self):
        NumO = 0
        NumX = 0
        
        #checks to see if either player has reached the end of the board.
        for n in range(len(self.boardPosition[0])):
            if self.boardPosition[0][n] == "O":
                winner = "O"
                self.Score = self.CalcWinner(winner)
                isDone = True 
                return isDone
            else:
                pass
        for n in range(len(self.boardPosition[7])):
            if self.boardPosition[7][n] == "X":
                winner = "X"
                self.Score = self.CalcWinner(winner)
                isDone = True 
                return isDone
            else:
                pass
            #checks to see if either side still has all their pieces.
         #runs through the entire board and counts up the number of O's
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m] == "O":
                    NumO = NumO + 1
                    
            #runs throught the entire board and counts up the total number of X's
        for n in range(len(self.boardPosition)):
            for m in range(len(self.boardPosition[n])):
                if self.boardPosition[n][m] == "X":
                    NumX = NumX + 1
                    
        if NumX == 0:
            winner = "O"
            self.Score = self.CalcWinner(winner)
            isDone = True 
            return isDone

        if NumO == 0:
            winner = "X"
            isDone = True 
            return isDone
        
        #changes the score based on how many pieces each side possesses. +1 for ai pieces and -1 for player pieces. At the start of the game should just be zero.
        PieceScore = NumX - NumO
        if self.IsRoot != True:
            self.Score = 0
            self.Score = self.Score + PieceScore
        else:
            pass

        return False
        


                        
                
#main
print("Welcome to simplified checkers")
print("This is a simplified version of checkers where you play against a computer.")
print("What makes it simplified is that the board is 4*8 instead of 8*8 and moves take via moving onto one another, instead of jumping over each other")
print("There are two ways to win this game: you can win via anihlation by taking all the opponents pieces, or you can win by simply getting to the other end of the board")
print("To make a move you have to say the column and row that the piece you want to move is on, then say if you want to move it left or right")
print("The columns are from 0 to 3, and the rows are from 0 to 7. The leftmost column is zero, and the top row is zero")
print("As stated previously, to take a piece you simply have to move ontop of it")
print("There may be a bit of a delay between moves, this shouldn't last longer than one minute")
print("With that being said good luck !!! You are playing as O")
while Done == False:
    print("===================================")
    displayboard(Board)
    print("====================================")
    print("====================================")
    Board = player1(Board)
    Done = checkwin(Board,NumX,NumO)
    if Done == True:
        break
    board1=BoardMinMax(Board,False, Score, True,0)
    Counter = 0
    Score = board1.children[0].Score
    HighScore = Score
    #best variables are to be set to the row and col that the new move is to be made.
    BestRow = 0
    BestCol = 0
    #Old Variables are to be set to the row and col were the piece that was moved used to be.
    OldRow = 0
    OldCol = 0
    #part that attempts to find the bestpossible move.
    for n in range(len(board1.children)):
        ChildBoard = board1.children[n].boardPosition
        Score = board1.children[n].Score
        #runs for as many times as there are children nodes of the root node.
        for n in range(len(ChildBoard)):
            #if the score of one of the children nodes is greater than the current highscore,
            #this board is searched through and the difference between this board and the previous board is found
            if Score > HighScore or Score == HighScore:
                HighScore = Score
                for n in range(len(Board)):
                #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
                #it finds the difference and returns the x y coordinates of this difference.
                    for m in range(len(Board[n])):
                        if Board[n][m] != ChildBoard[n][m]:
                            if ChildBoard[n][m] == "X":
                                BestRow = n
                                BestCol = m
                            elif ChildBoard[n][m] == "":
                                OldRow = n
                                OldCol = m

    Board[BestRow][BestCol] = "X"
    Board[OldRow][OldCol] = ""
    Done = checkwin(Board,NumX,NumO)




