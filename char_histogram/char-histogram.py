def char_histogram(s: str) -> dict[str, int]:
    """
    Return a dictionary mapping each character in s to the number of times it appears in the string.

    Parameters:
        s (str): The input string.

    Returns:
        dict[str, int]: A dictionary where keys are characters from s and 
                        values are the counts of those characters. 
    """
    
    dict = {}

    for symbol in s:
        if symbol in dict:
            dict[symbol] += 1
        else:
            dict[symbol] = 1
    
    return dict

