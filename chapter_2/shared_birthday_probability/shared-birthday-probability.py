import random # this should be helpful!

# Write your shared_birthday_probability() function here along with any subroutines that you need
def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials.

    Parameters:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """
    repeats = 0

    for _ in range(num_trials):
        if simulate_one_birthday_trial(num_people):
            repeats += 1

    return repeats / num_trials
