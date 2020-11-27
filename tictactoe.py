import pickle

STATES_FILE = './data/states.dat'
VALUE_FILE = './data/value.pickle'

class TicTacToe(object):

    def __init__(self, p1, p2):
        self.board = Board()
        self.p1 = p1
        self.p2 = p2

    def get_input(self, player):
        while True:
            row = input('Enter row: ')
            col = input('Enter col: ')
            try:
                row = int(row)
                col = int(col)

                return row, col
            except ValueError:
                print("This is not a number. Enter a digit between 1-9")

    def turn(self, player):
        print(f'Player {str(player)} turn.')
        while True:
            row, col = self.get_input(player)
            if self.board.move(row, col, player):
                return
            print('Input is invalid. Try again.')

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
        print(self.board)
        while score == 0 and self.board.has_move():
            self.turn(self.p1)
            print(self.board)

            score = self.score()
            if score != 0:
                break

            if not self.board.has_move():
                break

            self.turn(self.p2)
            print(self.board)

            score = self.score()
        if score == -1:
            print("Player 1 wins!")
        elif score == 1:
            print("Player 2 wins!")
        else:
            print("Draw.")

    def initValueFunction(self, new=True):
        #Attempt to read the states file
        value_table = {}
        if new:
            with open(STATES_FILE) as states:
                for board_state_str in states:
                    board_state_str = board_state_str[:-1]
                    self.board = Board(board_state_str)
                    score = self.score()
                    # Since we are X
                    value = 0.5
                    if score == -1:
                        value = 1.0
                    elif score == 1:
                        value = 0
                    value_table[board_state_str] = value
            with open(VALUE_FILE, 'wb') as handle:
                pickle.dump(value_table, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            # Read from value file and store in dict
            with open(VALUE_FILE, 'rb') as handle:
                value_table = pickle.load(handle)
        return value_table

    def initSimulation(self, new=True):
        self.value_table = self.initValueFunction(new)
        print(self.value_table)


class Player(object):

    def __init__(self, id=1):
        assert(id == 1 or id == 2)
        self._id = 'X' if id == 1 else 'O'

    def __str__(self):
        return self._id

class Board(object):
    EMPTY_SPACE = '-'

    def __init__(self, board_str=None):
        self.__move_count = 0
        if board_str:
            self.board_ = self.parse_board_str(board_str)
        else:
            self.board_ = [self.EMPTY_SPACE for i in range(9)]

    def move(self, row, col, player):
        if not self.validate(row, col):
            return False
        idx = 3 * row + col
        self.board_[idx] = str(player)
        self.__move_count += 1
        print(f'Move count: {self.__move_count}')
        return True

    def has_move(self):
        return self.__move_count < 9

    def validate(self, row, col):
        idx = 3 * row + col
        return self.has_move() and 0 <= row < 3 and 0 <= col < 3 \
            and 0 <= idx < 9 and self.board_[idx] == self.EMPTY_SPACE

    def state(self, row, col):
        return self.board_[3*row + col]

    def get_row(self, row):
        r = 3*row
        return ''.join(self.board_[r:r+3])

    def get_col(self, col):
        if col == 0:
            return self.board_[0] + self.board_[3] + self.board_[6]
        elif col == 1:
            return self.board_[1] + self.board_[4] + self.board_[7]
        else:
            return self.board_[2] + self.board_[5] + self.board_[8]

    def get_diag(self, diag):
        if diag == 0:
            return self.board_[0] + self.board_[4] + self.board_[8]
        else:
            return self.board_[2] + self.board_[4] + self.board_[6]

    def generate_all_board_states(self, idx):
        """
        Used only to generate a file once
        """
        if idx == 9:
            print(self.get_board_state_str())
            return

        for token in [self.EMPTY_SPACE, 'X' , 'O']:
            self.board_[idx] = token
            self.generate_all_board_states(idx + 1)

    def get_board_state_str(self):
        return ''.join(self.board_)

    def parse_board_str(self, board_str):
        return [s for s in board_str]

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
    game.initSimulation()

