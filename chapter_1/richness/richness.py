import sys
# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your richness() function here, along with any subroutines that you need.
def richness(sample: dict) -> int:
    """
    richness finds the total number of values in the table that are positive.

    Parameters:
    - sample (dict): A dictionary that contains integer values.

    Returns:
    - int: The total number of values that are greater than zero.
    """
    x = 0
    for val in sample.values():
        if val > 0:
            x += 1
    
    return x
    
