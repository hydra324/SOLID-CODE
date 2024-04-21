class Player:
    def __init__(self,id,marker) -> None:
        self.id = id
        self.marker = marker

class Move:
    def __init__(self,x,y,player: Player) -> None:
        self.x = x
        self.y = y
        self.player = player

class Board:
    def __init__(self,size) -> None:
        self.size = size
        self.state = None
        self.remianing_count = None
        self.reset()

    def reset(self):
        """ resets the board state """
        self.state = [[None for j in range(self.size)] for i in range(self.size)]
        self.remianing_count = 0

    def place_move(self,move: Move):
        if self.state[move.x][move.y]:
            raise ValueError("Illegal move, position already occupied")
        self.state[move.x][move.y] = move.player.marker

    
    def check_winner(self,last_move: Move) -> bool:
        if not last_move:
            return False
        return self.check_col(last_move.y,last_move.player) or \
                self.check_row(last_move.x,last_move.player) or \
                self.check_diag(last_move.x,last_move.y,last_move.player) or \
                self.check_cross_diag(last_move.x,last_move.y,last_move.player)

    def check_row(self,row:int,player: Player) -> bool:
        for j in range(self.size):
            if self.board[row][j] != player.marker:
                return False
        return True
    
    def check_col(self,col:int,player: Player) -> bool:
        for i in range(self.size):
            if self.board[i][col] != player.marker:
                return False
        return True
    
    def check_diag(self,row:int,col:int,player: Player) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if i-j != row-col:
                    continue
                if self.board[row][col] != player.marker:
                    return False
        return True
    
    def check_cross_diag(self,row:int,col:int,player: Player) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if i+j != row+col:
                    continue
                if self.board[row][col] != player.marker:
                    return False
        return True
    
    def is_over(self):
        return self.remianing_count==0

class Game:
    def __init__(self,player1: Player,player2: Player,board: Board) -> None:
        self.player1 = player1
        self.player2  = player2
        self.board = board

    def play_game(self):
        """ Simulates players playing the game """
        curr_player = self.player2
        last_move = None
        while self.board.is_over() or self.board.check_winner(last_move):
            curr_player = self.player2 if curr_player.id%2==1 else self.player1
            x = int(input(f"Enter player {curr_player.id}'s x move: "))
            y = int(input(f"Enter player {curr_player.id}'s y move: "))
            last_move = Move(x,y,curr_player)
            self.board.place_move(last_move)

        if self.board.check_winner(last_move):
            print(f'plaayer {curr_player.id} is the winner')
        else:
            print(f'game ended in a tie')


if __name__ == '__main__':
    player1 = Player(1,'X')
    player2 = Player(2,'O')
    board = Board(3)
    game = Game(player1,player2,board)
    game.play_game()

        