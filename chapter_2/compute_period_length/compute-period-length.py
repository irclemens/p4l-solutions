# Write your compute_period_length() function here along with any subroutines that you need
def compute_period_length(a: list[int]) -> int:
    """
    Compute the period length of a list of integers.

    Parameters:
    - a: a list of integers

    Returns:
    int: the length of the period of a
    """
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                return j - i
    
    return 0
