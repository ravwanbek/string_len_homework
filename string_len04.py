def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    n=len(s)
    b="\u002A"*n
    return b
print(main(s='hello'))