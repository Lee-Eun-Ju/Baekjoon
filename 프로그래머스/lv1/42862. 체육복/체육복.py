# n:전체 학생의 수, lost:체육복을 도난당한 학생들 번호
# reserve:여벌의 체육복을 가져온 학생들 번호

def solution(n, lost, reserve):
    
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)
        
    count = 0
    for x in l:
        # 첫번째 학생은 제외하고, 왼쪽 학생 탐색
        if (x-1) != 0 and (x-1) in r:
            r.remove(x-1)
        # 마지막 학생은 제외하고, 오른쪽 학생 탐색
        elif (x+1) != n+1 and (x+1) in r:
            r.remove(x+1)
        else:
            count += 1
        
    return n - count