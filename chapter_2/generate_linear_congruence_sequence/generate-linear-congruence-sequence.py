# Write your generate_linear_congruence_sequence() function here along with any subroutines that you need.
def generate_linear_congruence_sequence(seed: int, a: int, c: int, m: int) -> list[int]:
    """
    Generate a linear congruence sequence.

    Parameters:
    - seed (int): the first value in the sequence
    - a (int): the multiplier
    - c (int): the increment
    - m (int): the modulus

    Returns:
    list: a sequence of integers produced by the linear congruential generator
    """
    sequence = [seed]

    while not has_repeat(sequence):
        next_value = (a * sequence[-1] + c) % m
        sequence.append(next_value)

    return sequence
