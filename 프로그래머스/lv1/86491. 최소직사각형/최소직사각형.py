def solution(sizes):
    
    # 가로 길이가 큰 값이도록 위치 변경
    for x in sizes:
        a = x[0]
        b = x[1]
        if x[0] < x[1]:
            x[0] = b
            x[1] = a
    
    width = [x[0] for i,x in enumerate(sizes)]  # 가로
    length = [x[1] for i,x in enumerate(sizes)] # 세로
    
    max_w = max(width)
    max_l = max(length)
    
    answer = max_w*max_l
    return answer