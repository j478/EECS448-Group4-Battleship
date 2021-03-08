class Power:
    """
    @pre - Difficulty selected.
    @param row - Row of power-up.
    @param col - Column of power-up.
    @param difficulty - Integer. Easy (0), medium (1), or hard (2).
    """
    def __init__(self, row, col, difficulty):
        self.row = row
        self.col = col
        self.difficulty = difficulty
        self.was_used = False
