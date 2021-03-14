class Power:
    # @pre - Difficulty selected.
    # @param - row, column, level of difficulty (easy = 1, medium = 2, hard = 3)
    # @post - None
    # @return - None
    def __init__(self, row, col, difficulty):
        print("Demo mode: Power up added at row", row, ", column ", col)
        assert difficulty in range(1, 4)  # Test difficulty is reasonable.

        self.row = row
        self.col = col
        self.difficulty = difficulty

        self.was_hit = False
        self.active = False

    # @pre - Power-up active.
    # @param - clicked_row, clicked_column are the squares the user chooses.
    # @post - None
    # @return - A list of tuples indicating where the power-up lets the user hits.
    def squares(self, clicked_row, clicked_col):
        assert self.active  # Testing: make sure only called when active.

        if self.difficulty == 1:
            return self.easy_squares(clicked_row, clicked_col)
        elif self.difficulty == 2:
            return self.medium_squares(clicked_row, clicked_col)
        elif self.difficulty == 3:
            return self.hard_squares(clicked_row, clicked_col)

    # @pre - Power-up active.
    # @param - clicked_row, clicked_column are the squares the user chooses.
    # @post - None
    # @return - A list of tuples indicating where the power-up lets the user hits.
    def easy_squares(self, clicked_row, clicked_col):
        reached = [(clicked_row-1, clicked_col-1),
                   (clicked_row-1, clicked_col),
                   (clicked_row-1, clicked_col+1),
                   (clicked_row, clicked_col-1),
                   (clicked_row, clicked_col),
                   (clicked_row, clicked_col+1),
                   (clicked_row+1, clicked_col-1),
                   (clicked_row+1, clicked_col),
                   (clicked_row+1, clicked_col+1)]
        return self.trimmed_list(reached)

    # @pre - Power-up active.
    # @param - clicked_row, clicked_column are the squares the user chooses.
    # @post - None
    # @return - A list of tuples indicating where the power-up lets the user hits.
    def medium_squares(self, clicked_row, clicked_col):
        rows = [r for r in range(clicked_row-10, clicked_col+10)]
        cols = [c for c in range(clicked_row-10, clicked_col+10)]
        reached_vert = zip(rows, [clicked_col]*len(cols))
        reached_hor = zip([clicked_row]*len(rows), cols)

        return self.trimmed_list(list(reached_vert) + list(reached_hor))

    # @pre - Power-up active.
    # @param - clicked_row, clicked_column are the squares the user chooses.
    # @post - None
    # @return - A list of tuples indicating where the power-up lets the user hits.
    def hard_squares(self, clicked_row, clicked_col):
        main_diag_squares = list()
        other_diag_squares = list()

        for i in range(-10, 10):
            main_diag_squares.append((clicked_row-i, clicked_col-i))
            other_diag_squares.append((clicked_row-i, clicked_col+i))

        diag_squares = main_diag_squares + other_diag_squares

        return self.trimmed_list(diag_squares + self.medium_squares(clicked_row, clicked_col))

    # @pre - Power-up active.
    # @param -
    # @post - None
    # @return -
    def trimmed_list(self, square_list):
        return list([s for s in square_list if (0 <= s[0] <= 9 and 0 <= s[1] <= 9)])
