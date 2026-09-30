# Write your generate_middle_square_sequence() function here along with any subroutines that you need.
def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    """
    Generate a middle square sequence.

    Parameters:
    - seed (int): the first value in the sequence
    - num_digits (int): the number of digits in the middle of each squared value to add to the sequence

    Returns:
    list: a middle-square sequence
    """
    sequence = [seed]

    while not has_repeat(sequence):
        next_value = square_middle(sequence[-1], num_digits)
        sequence.append(next_value)

    return sequence
