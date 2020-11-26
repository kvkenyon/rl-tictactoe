

class TicTacToe(object):
    pass

class Player(object):

    def __init__(self, id=1):
        assert(id == 1 or id == 2)
        self._id = 'X' if id == 1 else 'O'

    def __str__(self):
        return self._id

class Board(object):
    EMPTY_SPACE = '-'

    def __init__(self):
        self.board_ = [self.EMPTY_SPACE for i in range(9)]

    def move(self, row, col, player: Player):
        assert(0 <= row < 3)
        assert(0 <= col < 3)
        idx = 3 * row + col
        assert(0 <= idx < 9)
        self.board_[idx] = str(player)

    def __str__(self):
        result = ''
        for i in range(3):
            for j in range(3):
                result += self.board_[3*i+j] + ' '
            result += '\n'
        return result


if __name__ == "__main__":
    p1 = Player(1)
    p2 = Player(2)


    board = Board()
    board.move(0,0,p1)
    board.move(1,1,p2)
    print(board)
