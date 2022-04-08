def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    sum_odds=0
    for i in range(N+1):
        if i%2==1:
            sum_odds+=i
    return sum_odds