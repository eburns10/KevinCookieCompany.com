### clases that we need to create
### board class
### player class


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


    def __str__(self):
        return(f"Player {self.name} who is {self.symbol}")
    

class Board:
    emptySpace = "."
    size = 3

    def __init__(self):
        self.board = [[self.emptySpace] * self.size for i in range(0, self.size)]

    def __str__(self):
        strRepresent = ["".join(x) for x in self.board]
        ####tells to join each . in each mini list giving a list of 3 values that are each ...
        strRepresent = "\n".join(strRepresent)
        #### joins each ... with a line break in between to make board
        return(strRepresent)

    def checkVictory(self, player):
        sym = player.symbol
        successList = [sym] * self.size


        # diagonal check
        topLeftToBottomRight = [self.board[i][i] for i in range(0, self.size)]
        bottomLeftToTopRight = [self.board[i][self.size - 1 - i] for i in range(0, self.size)]

        diagonalPass = topLeftToBottomRight == successList or bottomLeftToTopRight == successList
        if diagonalPass:
            return (True)
        
        # row check
        for row in self.board:
            if row == successList:
                return(True)
            
        # column check
        for i in range(0, self.size):
            col = [self.board[row] for row in range(0, self.size)]
            if col == successList:
                return(True)
            
        return(False)



        
    
    def markBoard(self, player, coord):
        row = coord[0]
        col = coord[1]

        if row < 0 or row >= self.size:
            print("Row coordinate out of bounds. Try again.")
            return(None)
        
        elif col < 0 or col >= self.size:
            print("Col coordinate is out of bounds. Try agai.")
            return(None)
        
        if self.board[row][col] != self.emptySpace:
            print("Current coordinate is already been taken. Try again.")
            return(None)
        
        ### everything now pases, so let's mark the board
        self.board[row][col] = player.symbol

        return(self.checkVictory(player))
    

def promptPlayerTurn(player, board):
    successfulTurn = False
    
    while not successfulTurn:
        coord = input(f"Player {player}, please enter coordinates (i.e 0,2): ")

        coordList = coord.split(",")
        if len(coordList) != 2:
            print("Coordinate nomenclature not correct. Try again.\n")
            continue

        try:
            coordList = [int(x) for x in coordList]
            check = board.markBoard(player, coordList)
            

            if check is not None:
                successfulTurn = True
                return(check)


        except ValueError:
            print("Coordinate input was not an integer. Try again. \n")

    

def createPlayer(playerNumber, symbol):
    name = input(f"Player {playerNumber}, you will be {symbol}. What is your name: ")
    p = Player(name, symbol)

    return p

def main():
    p1 = createPlayer(1, "X")
    p2 = createPlayer(2, "O")

    print(p1)
    print(p2)
    gameBoard = Board()
    print(gameBoard)

    print(f"Welcome to tic tac toe, {p1} and {p2}")
    print("This is the current board")
    print(gameBoard)

    gameFinished = False
    while not gameFinished:
        p1Turn = promptPlayerTurn(p1, gameBoard)
        print(gameBoard)

        if p1Turn:
            print(f"Game Fininshed. {p1} has won!")
            gameFinished = True
            continue
        
        p2Turn = promptPlayerTurn(p2, gameBoard)
        print(gameBoard)

        if p2Turn:
            print(f"Game Finished. {p2} has won!")
            gameFinished = True
            continue

main()
