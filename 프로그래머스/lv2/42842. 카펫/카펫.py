def solution(brown, yellow):
    
    # 2x + 2y + 4 = brown
    # x*y = yellow   
    xy_sum = (brown - 4)//2
    xy_mul = yellow
    
    answer = []
    for x in range(1,xy_sum//2+1):
        if x*(xy_sum-x) == xy_mul:
            answer.append(xy_sum-x+2)
            answer.append(x+2)
            break
            
    return answer