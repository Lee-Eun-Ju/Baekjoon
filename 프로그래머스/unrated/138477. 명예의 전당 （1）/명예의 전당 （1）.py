def solution(k, score):
    answer = []
    
    if k>len(score):
        for x in range(1,len(score)+1):
            answer.append(min(score[0:x]))
            
    else:
        for j in range(1,k+1):
            answer.append(min(score[0:j]))

        for i in range(k+1,len(score)+1):
            data = sorted(score[0:i], reverse=True)
            answer.append(data[k-1])

    answer
    return answer