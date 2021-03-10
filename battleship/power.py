class Power:
    # @pre - Difficulty selected.
    # @param - row, colum, level of difficulty (easy = 0, medium = 1, hard = 2)
    # @post - None
    # @return -None
    def __init__(self, row, col, difficulty):
        self.row = row
        self.col = col
        self.difficulty = difficulty
        self.was_used = False
