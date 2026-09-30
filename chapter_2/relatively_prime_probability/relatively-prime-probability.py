import random # this should be helpful!

# Write your relatively_prime_probability() function here along with any subroutines that you need
# Hint: include your relatively_prime() function and any subroutines that it calls.
def relatively_prime_probability(
    lower_bound: int,
    upper_bound: int,
    num_pairs: int
) -> float:    
    """
    Compute the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime.

    Parameters:
    - lower_bound (int): the lower bound of the range
    - upper_bound (int): the upper bound of the range
    - num_pairs (int): the number of pairs to trial

    Returns:
    float: the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime
    """
    relatively_prime_count = 0

    for _ in range(num_pairs):
        a = random.randint(lower_bound, upper_bound)
        b = random.randint(lower_bound, upper_bound)

        if relatively_prime(a, b):
            relatively_prime_count += 1

    return relatively_prime_count / num_pairs
