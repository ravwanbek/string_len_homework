def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    a=len(s1)
    b=len(s2)


    if a>=b:
        return b
    else: 
        return a
    
print(main(s1='Alisher',s2='Sardor'))
