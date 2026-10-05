def change_mask(board: list[list[bool]]) -> list[list[bool]]:
    """
    Given a Game of Life board, return a mask grid of the same size whose entries
    are True exactly at cells that will change state in the next generation.
    Args:
        board (GameBoard = list[list[bool]] ): A rectangular Game of Life board.

    Returns:
        list[list[bool]]: A grid of the same dimensions, where mask[r][c] is True
                          if and only if update_cell(board, r, c) != board[r][c].
    """
    mask = []

    for row in range(len(board)):
        mask_row = []
        for col in range(len(board[row])):
            mask_row.append(update_cell(board, row, col) != board[row][col])
        mask.append(mask_row)

    return mask
