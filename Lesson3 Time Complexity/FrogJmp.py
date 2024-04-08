import math

def solution(X, Y, D):
    dis = Y - X #差多少距離
    return math.ceil(dis/D) #最少需要幾步
