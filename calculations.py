import math


def slowSumStringLengthOfXinN(n):
    __doc__ = ''' Function for calculating the string length of the concatenation
    of every number in n ,
    becomes time and memory consuming when n gets big'''
    s=''
    for i in range(n):
        s += str(i)
    return len(s)

def fastSumStringLengthOfXinN(N):
    __doc__ = ''' Function for calculating the string length of the concatenation
        of every number in n ,
        uses artimetic to calculate the length, its memory efficient
        Designed by: Paal S. Pedersen
        on Sunday 23 of september 2018'''
    if N < 10:
        return N
    else:
        # N > 10!
        # n = int(math.log10(103)) = 2
        trailing_n = int(math.log10(N))
        # (103 - 100) = 3
        r = (N - 10 ** (trailing_n))
        # unknown general math name of a number starting with 1 and has only trailing 0
        # We will give this number the name: The Paalion number
        # (103 - 3) = 100
        paalion = N - r
        # unknown general math name of the number in curly bracket, example 9100 - {8100} = 1000
        # We will name this number the rosalion number
        rosalion = r * (trailing_n + 1)
        def lengthOfPaalion(local_paalion):
            if local_paalion <= 10:
                return 10
            else:
                # 10 + (100-10) * 2 = 10 + 90*2 = 190
                return lengthOfPaalion(local_paalion // 10) + (local_paalion - local_paalion // 10)\
                       * int(math.log10(local_paalion))
        # 9 + 190
        return rosalion + lengthOfPaalion(paalion)

