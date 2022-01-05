def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)
    b=len(s2)
    c=len(s3)
    if a%2!=0 and b%2==0 and c%2==0:
        answer=[s1]
    elif b%2!=0 and a%2==0 and c%2==0:
        answer=[s2]
    elif c%2!=0 and a%2==0 and b%2==0:
        answer=[s3]
    elif a%2!=0 and b%2!=0 and c%2==0:
        answer=[s1,s2]
    elif a%2!=0 and c%2!=0 and b%2==0:
        answer=[s1,s3]
    elif b%2!=0 and c%2!=0 and a%2==0:
        answer=[s2,s3]
    elif a%2!=0 and b%2!=0 and c%2!=0:
        answer=[s1,s2,s3]
    
    return answer   
print(main(s1='Kia',s2='Toyota',s3='BMW'))


        



    