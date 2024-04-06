import math

def solution(X, Y, D):
    dis = Y - X
    return math.ceil(dis/D)