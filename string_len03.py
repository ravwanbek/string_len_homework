def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    c=''

    if len(a)==len(b):
        c=True
    else:
        c=False

    return c
print(main(a='Ali',b='ali'))