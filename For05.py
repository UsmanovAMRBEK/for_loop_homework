def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    answer=[]
    for i in range(B,A-1,-1):
        answer.append(i)
    return answer
n=5;m=9
print(main(n,m))