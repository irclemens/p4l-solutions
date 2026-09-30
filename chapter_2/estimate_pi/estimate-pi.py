import random # this should be helpful!

# Write your estimate_pi() function here along with any subroutines that you need.
def estimate_pi(num_points: int) -> float:
    """
    Estimate pi using a Monte Carlo method.

    Parameters:
    - num_points (int): the number of points to use in the Monte Carlo method

    Returns:
    float: an estimate of pi
    """
    inside = 0

    for _ in range(num_points):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1

    return 4.0 * inside / num_points
