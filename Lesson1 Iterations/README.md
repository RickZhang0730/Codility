# BinaryGap
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

'
def solution(N):
    list_A = bin(N)[2:] #轉成二進制，例如bin(10)為0b1010，去掉0b
    max_gap = 0
    current_gap = 0

    for x in list_A:
        if x == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap
#如果進來的是10000，那一開始max_跟current_gap為0，之後一直遇到0，current_gap=4，但沒有遇到1就不會更新max_gap，因此return max_gap=0
#如果進來的是10010，那1進來，max_gap=0，current_gap=0，下兩個0進來，current_gap=2，再遇到1，max_gap=2，current_gap=0，再遇到0，current_gap=1，最終return max_gap=2
'
