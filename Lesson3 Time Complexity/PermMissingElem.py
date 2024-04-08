def solution(A):
    N = len(A)
    total_sum = (1 + (N + 1))*(N + 1) // 2  #正常總和
    array_sum = sum(A) #目前總和
    x = total_sum - array_sum #找到所缺失的
    return x
