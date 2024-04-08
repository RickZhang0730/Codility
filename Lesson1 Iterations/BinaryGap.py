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
