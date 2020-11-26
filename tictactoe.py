
class TicTacToe(object):

    def __init__(self, p1, p2):
        self.board = Board()
        self.p1 = p1
        self.p2 = p2

    def turn(self, player):
        print(f'Player {str(player)} turn.')
        row = input('Enter row: ')
        col = input('Enter col: ')
        return int(row), int(col)

    def score(self):
        p1_token = str(self.p1)
        p2_token = str(self.p2)
        winp1 = 3 * p1_token
        winp2 = 3 * p2_token
        diag = self.board.get_diag(0)
        adiag = self.board.get_diag(1)

        if diag == winp1:
            return -1
        if diag == winp2:
            return 1
        if adiag == winp1:
            return -1
        if adiag == winp2:
            return 1

        for i in range(3):
            row = self.board.get_row(i)
            col = self.board.get_col(i)
            if row == winp1:
                return -1
            if row == winp2:
                return 1
            if col == winp1:
                return -1
            if col == winp2:
                return 1

        return 0

    def run(self):
        score = self.score()
        while score == 0:
            print(self.board)
            row, col = self.turn(p1)
            self.board.move(row, col, p1)
            print(self.board)
            score = self.score()
            row, col = self.turn(p2)
            self.board.move(row, col, p2)
            print(self.board)
            score = self.score()
        if score == -1:
            print("Player 1 wins!")
        elif score == 1:
            print("Player 2 wins!")
        else:
            print("Draw.")


class Player(object):

    def __init__(self, id=1):
        assert(id == 1 or id == 2)
        self._id = 'X' if id == 1 else 'O'

    def __str__(self):
        return self._id

class Board(object):
    EMPTY_SPACE = '-'

    def __init__(self):
        self.__move_count = 0
        self.board_ = [self.EMPTY_SPACE for i in range(9)]

    def move(self, row, col, player):
        assert(self.__move_count < 9)
        assert(0 <= row < 3)
        assert(0 <= col < 3)
        idx = 3 * row + col
        assert(0 <= idx < 9)
        assert(self.board_[idx] == self.EMPTY_SPACE)
        self.board_[idx] = str(player)
        self.__move_count += 1

    def state(self, row, col):
        return self.board_[3*row + col]

    def get_row(self, row):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        r = 3*row
        return ''.join(self.board_[r:r+3])

    def get_col(self, col):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        if col == 0:
            return self.board_[0] + self.board_[3] + self.board_[6]
        elif col == 1:
            return self.board_[1] + self.board_[4] + self.board_[7]
        else:
            return self.board_[2] + self.board_[5] + self.board_[8]

    def get_diag(self, diag):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        if diag == 0:
            return self.board_[0] + self.board_[4] + self.board_[8]
        else:
            return self.board_[2] + self.board_[4] + self.board_[6]


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
    game = TicTacToe(p1, p2)
    game.run()

