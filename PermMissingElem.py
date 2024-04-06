def solution(A):
    N = len(A)
    total_sum = (1 + (N + 1))*(N + 1) // 2
    array_sum = sum(A)
    x = total_sum - array_sum
    return x