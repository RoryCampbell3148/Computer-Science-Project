#version 1.0: a limited 2 player version of checkers. Board is 8 long by 4 across. You win by anihlation or by reaching the end.
#pieces take by moving onto one another, instead of jumping over each other.
#the starting board of the game.
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
for n in range(len(Board)):
    print(Board[n])

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
    
    
    


                        
                
#main            
while Done == False:
    player1(Board)
    Done = checkwin(Board,NumX,NumO)
    if Done == True:
        break
    player2(Board)
    Done = checkwin(Board,NumX,NumO)
