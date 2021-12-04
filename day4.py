BOARD_COLUMN_COUNT = 5
BOARD_ROW_COUNT = 5
class Board:
    def __init__(self) -> None:
        self.columns_hit_count = BOARD_COLUMN_COUNT * [0]
        self.rows_hit_count = BOARD_ROW_COUNT * [0]
        self.numbers = [[None] * BOARD_COLUMN_COUNT for _ in range(BOARD_ROW_COUNT)]
        self.numbers_hit = [[False] * BOARD_COLUMN_COUNT
                            for _ in range(BOARD_ROW_COUNT)]
        self.row_of_last_added_no = 0
        self.column_of_last_added_no = -1

    def add_number(self, number):
        self.column_of_last_added_no += 1
        if self.column_of_last_added_no == BOARD_COLUMN_COUNT:
            self.column_of_last_added_no = 0
            self.row_of_last_added_no += 1
            assert(self.row_of_last_added_no < BOARD_ROW_COUNT)
        self.numbers[self.row_of_last_added_no][self.column_of_last_added_no] = number

    def register_draw(self, number):
        for r_idx, row in enumerate(self.numbers):
            for c_idx, num in enumerate(row):
                if number == num:
                    if not self.numbers_hit[r_idx][c_idx]:
                        self.numbers_hit[r_idx][c_idx] = True
                        self.rows_hit_count[r_idx] += 1
                        self.columns_hit_count[c_idx] += 1
                        if self.rows_hit_count[r_idx] == BOARD_ROW_COUNT:
                            return True
                        if self.columns_hit_count[c_idx] == BOARD_COLUMN_COUNT:
                            return True
        return False

    def sum_of_unmarked_numbers(self):
        total = 0
        for r_idx, row in enumerate(self.numbers):
            for c_idx, num in enumerate(row):
                if not self.numbers_hit[r_idx][c_idx]:
                    total += num
        return total

    def __repr__(self) -> str:
        return f"{self.columns_hit_count= }, {self.rows_hit_count= }, {self.numbers =}, {self.numbers_hit =}, {self.row_of_last_added_no= }, {self.column_of_last_added_no= }"


boards = list()
with open('day4.txt') as f:
    drawn_numbers = f.readline()
    boards_text = f.readlines()

no_boards = 0
for line in boards_text:
    if line == "\n":
        new_board = Board()
        no_boards +=1
        boards.append(new_board)
    else:
        for num in line.split():
            boards[no_boards-1].add_number(int(num))

print(f"{len(boards)= }")
winners = list()
first_winning_draw = None
last_winning_draw = None
for draw in drawn_numbers.split(","):
    for board in boards:
        if board in winners:
            continue
        if board.register_draw(int(draw)):
            winner_board = board
            winners.append(board)
            if first_winning_draw is None:
                first_winning_draw = int(draw)
            last_winning_draw = int(draw)
            print(f"Winning draw {draw}")
    #         break
    # if winner_board is not None:
    #     break

print(f"{winners[0].sum_of_unmarked_numbers() = }")
print(f"final score {winners[0].sum_of_unmarked_numbers() * first_winning_draw}")
print(f"{winners[len(winners) - 1].sum_of_unmarked_numbers() = }")
print(f"final score {winners[len(winners) - 1].sum_of_unmarked_numbers() * last_winning_draw}")


