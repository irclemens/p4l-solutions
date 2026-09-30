import random # this should be helpful!

# Write your simulate_one_birthday_trial() function here along with any subroutines that you need
def simulate_one_birthday_trial(num_people: int) -> bool:
    """
    Simulate one trial of the birthday game with num_people people.

    Parameters:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """

    birthdays = []

    birthdays = []

    for _ in range(num_people):
        birthday = random.randint(1, 365)

        if birthday in birthdays:
            return True

        birthdays.append(birthday)

    return False
