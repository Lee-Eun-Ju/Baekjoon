# progresses  배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
# speeds  각 작업의 개발 속도가 적힌 정수 배열

def solution(progresses, speeds):
    
    from collections import deque
    day = deque()
    
    for i, x in enumerate(progresses):
        y = 100 - x
        if y%speeds[i] == 0:
            day.append(y//speeds[i])
        else:
            day.append(y//speeds[i] + 1)
    
    answer = []
    answer_day = []
    day_list = list(day)
    
    for i,x in enumerate(day_list):
        x = day.popleft()
        if len(answer)==0:
            answer.append(1)
            answer_day.append(x)
        elif answer_day[-1] >= x:
            answer[-1] += 1
        else:
            answer.append(1)
            answer_day.append(x)
        
    return answer