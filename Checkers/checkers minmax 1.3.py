#Version 1.3. The computer is only able to look forward by a set number of moves so that turns take less time.
#Version 1.2 placed the function that figures out what child has the highest score and what move has been made on this board outside of a function and directly into main.
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
    return Board 

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
#checks to see if either player has reached the end of the board.
    for n in range(len(Board[0])):
        if Board[0][n] == "O":
            print("O WINS")
            return True
        else:
            pass
    for n in range(len(Board[7])):
        if Board[7][n] == "X":
            print("X WINS")
            for n in range(len(Board)):
                print(Board[n])
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
        return True
    if NumO == 0:
        print("X WINS")
        for n in range(len(Board)):
            print(Board[n])
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
            #print("===")
            #print(Score)
            #print(HighScore)
            #print("===")
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
                            #print(n)
                            #print(m)
                            BestRow = n
                            BestCol = m
                        elif board1[n][m] == "":
                            #print(n)
                            #print(m)
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
        Counter = Counter + 1
        if self.IsRoot == True:
            print(Counter)
        #if self.Score == -10:
        #    print("======================================================")
        #    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #    for n in range(len(self.boardPosition)):
        #        print(self.boardPosition[n])
        #    print("======================================================")
        #if self.Score != 0:
            #print(self.Score)
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
            #if the number of children before it is a set value, then children will not be generated.
            #this is to stop the ai taking too long between turns.
            if self.NumChild < 8:
                self.NumChild = self.NumChild + 1
                #print(self.NumChild)
                self.GenerateChildren()
                #if the board is not the root, then it creates its score based off of the scores of its children.
                #This is only calculated after all children are created. 
                if self.IsRoot == False:
                    #if the player is the minimising, takes the lowest score of the children nodes
                    #if maximising, instead takes the highest score.
                    for n in range(len(self.children)):
                        if isO == False:
                            if self.children[n].Score > self.Score:
                                #print("=============")
                                #print(self.children[n].Score)
                                self.Score=self.children[n].Score
                                #print(self.Score)
                                #print("=============")
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
    
    #test method to add a child board
    #creates a new child board according to the current board position.
    def AddChild(self, boardpos):
        #create a new board out of the minmax constructor.
        #not self.NextisO is used to flip the turn.
        newBoard=BoardMinMax(boardpos,not self.NextisO)
        #adds the new board to the list of children boards.
        self.children.append(newBoard)
        #print(self.children)
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
                                newBoard=BoardMinMax(newBoardPos, not self.NextisO, Score,False,self.NumChild)
                            #adds the newly created board to the children boards list. 
                                self.children.append(newBoard)
                                #for n in range(len(Board)):
                                 #   print(Board[n])
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
                #print(self.Score)
                #print("O wins")
                isDone = True 
                return isDone
            else:
                pass
        for n in range(len(self.boardPosition[7])):
            if self.boardPosition[7][n] == "X":
                winner = "X"
                self.Score = self.CalcWinner(winner)
                #print(self.Score)
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
            self.Score = self.CalcWinner(winner)
            #print(self.Score)
            isDone = True 
            return isDone
        
        #changes the score based on how many pieces each side possesses. +1 for ai pieces and -1 for player pieces. At the start of the game should just be zero.
        PieceScore = NumX - NumO
        if self.IsRoot != True:
            self.Score = 0
            self.Score = self.Score + PieceScore
            #if self.Score < -6:
            #    print(PieceScore)
            #    print("=======================")
            #    for m in range(len(self.boardPosition)):
            #        print(self.boardPosition[m])
            #    print(self.Score)
            #    print("=======================")
        else:
            pass

        return False
        


                        
                
#main            
while Done == False:
    for n in range(len(Board)):
        print(Board[n])
    Board = player1(Board)
    Done = checkwin(Board,NumX,NumO)
    if Done == True:
        break
    board1=BoardMinMax(Board,False, Score, True,0)
    #print(Counter)
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
    #print("AAAAAA")
    #print(len(board1.children))
    for n in range(len(board1.children)):
        print("=======================")
        for m in range(len(Board)):
            print(board1.children[n].boardPosition[m])
        print(board1.children[n].Score)
        print("=======================")
        ChildBoard = board1.children[n].boardPosition
        Score = board1.children[n].Score
        #runs for as many times as there are children nodes of the root node.
        for n in range(len(ChildBoard)):
            #if the score of one of the children nodes is greater than the current highscore,
            #this board is searched through and the difference between this board and the previous board is found
            if Score > HighScore or Score == HighScore:
                #print("===")
                #print(Score)
                #print(HighScore)
                #print("===")
                HighScore = Score
                #print("===")
                #print(HighScore)
                #print("===")
                for n in range(len(Board)):
                #this takes the highscore board, so the board with the best possible move, and compares it to the current board state.
                #it finds the difference and returns the x y coordinates of this difference.
                    for m in range(len(Board[n])):
                        if Board[n][m] != ChildBoard[n][m]:
                            if ChildBoard[n][m] == "X":
                                #print(n)
                                #print(m)
                                BestRow = n
                                BestCol = m
                            elif ChildBoard[n][m] == "":
                                #print(n)
                                #print(m)
                                OldRow = n
                                OldCol = m

    Board[BestRow][BestCol] = "X"
    Board[OldRow][OldCol] = ""
    Done = checkwin(Board,NumX,NumO)



