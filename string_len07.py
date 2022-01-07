def main(s1,s2,s3):
    """
    Given three ngs, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: ng
        s2: ng
        s3: ng
    Returns:
        string
    """
    s1=str(s1)
    s2=str(s2)
    s3=str(s3)
    a=len(s1)
    b=len(s2)
    c=len(s3)

    if a%2!=0 and b%2==0 and c%2==0:
        answer=f'{s1}'
    elif b%2!=0 and a%2==0 and c%2==0:
        answer=f'{s2}'
    elif c%2!=0 and a%2==0 and b%2==0:
        answer=f'{s3}'
    elif a%2!=0 and b%2!=0 and c%2==0:
        answer='['+f'{s1}'+','+' '+f'{s2}'+']'
    elif a%2!=0 and c%2!=0 and b%2==0:
        answer='['+f'{s1}'+','+' '+f'{s3}'+']'
    elif b%2!=0 and c%2!=0 and a%2==0:
        answer='['+f'{s2}'+','+' '+f'{s3}'+']'
    elif a%2!=0 and b%2!=0 and c%2!=0:
        answer='['+f'{s1}'+','+' '+f'{s2}'+','+' '+f'{s3}'+']'
    elif a%2==0 and b%2==0 and c%2==0:
        answer='[]'
    
    return answer   
print(main('kiaa','hyundaia','audi'))


        



    