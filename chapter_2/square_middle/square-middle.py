# Write your square_middle() function here along with any subroutines that you need.
def square_middle(x, num_digits):
    """
    Get the middle digits of x squared.

    Parameters:
    - x (int): a positive integer
    - num_digits (int): the number of digits in the middle of x squared to return

    Returns:
    int: the middle digits of x squared
    """
    if x < 0 or num_digits <= 0 or num_digits % 2 != 0:
        return -1

    if count_num_digits(x) > num_digits:
        return -1

    squared = x ** 2
    squared = str(squared).zfill(2 * num_digits)

    start = num_digits // 2
    return int(squared[start:start + num_digits])
