import sys,getopt

class Game(object):

    def __init__(self, state, infinite_board = True):

        self.state = state
        self.width = state.width
        self.height = state.height
        self.infinite_board = infinite_board

    def isNotInRange(self, x, y):
        count = 0
        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if (0 <= x + hor < self.width and 0 <= y + ver < self.height) == False and self.state.board[y][x] == 1:
                    count += 1
        return count

    def generateNewBoard(self):
        new_Board = [[0] * (self.width +2) for i in range(self.height + 2)]

        for y, row in enumerate(self.state.board):
            for x, cell in enumerate(row):
                new_Board[y + 1][x + 1] = self.state.board[y][x]

        return new_Board

    def step(self, count=1):

        for generation in range(count):
            count = 0
            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    count += self.isNotInRange(x, y)

            if (count > 0):
                self.state.board = self.generateNewBoard()
                self.width = len(self.state.board)
                self.height = len(self.state.board[0])

            new_board = [[False] * self.width for row in range(self.height)]

            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    neighbours = self.neighbours(x, y)
                    previous_state = self.state.board[x][y]
                    should_live = neighbours == 3 or (neighbours == 2 and previous_state == True)
                    new_board[x][y] = should_live

            self.state.board = new_board

    def neighbours(self, x, y):

        count = 0

        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and (0 <= x + hor < self.width and 0 <= y + ver < self.height) and \
                                self.state.board[x + hor][y + ver] == 1:
                    count += 1

        return count

    def display(self):
        return self.state.display()

class State(object):

    def __init__(self, positions, width, height):

        active_cells = []

        for y, row in enumerate(positions):
            for x, cell in enumerate(row.strip()):
                if cell == '1':
                    active_cells.append((x,y))

        board = [[False] * width for row in range(height)]

        for cell in active_cells:
            board[cell[1]][cell[0]] = True

        self.board = board
        self.width = width
        self.height = height

    def display(self):

        output = ''

        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    output += ' 1'
                else:
                    output += ' 0'
            output += '\n'

        return output

# Store input and output file names
ifile=''
ofile=''
# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:n:o:")

def get_glider():
   glider_file = open(sys.argv[2], 'r')
   glider = glider_file.read().splitlines()
   glider_file.close()

   return glider

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
   if o == '-i':
       glider = get_glider()
       rows = len(glider)
       columns = len(glider[0])
       my_game = Game(State(glider, width = rows, height = columns))
   if o == '-n':
       nr_iter = int(a)
   if o == '-o':
       with open(sys.argv[6], 'wb+') as ofile:
           my_game.step(nr_iter)
           ofile.write(my_game.display())
           ofile.close()