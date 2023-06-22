# 1번 수포자 1,2,3,4,5
# 2번 수포자 2,1,2,3,2,4,2,5
# 3번 수포자 3,3,1,1,2,2,4,4,5,5

def solution(answers):
    
    n = len(answers)
    a = [1,2,3,4,5] 
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5] 
    
    a_answer = a*(n//5) + a[0:(n%5)]
    b_answer = b*(n//8) + b[0:(n%8)]
    c_answer = c*(n//10) + c[0:(n%10)]
    
    result = [0,0,0]
    
    for i, x in enumerate(answers):        
        if x == a_answer[i]:
            result[0] += 1
        if x == b_answer[i]:
            result[1] += 1
        if x == c_answer[i]:
            result[2] += 1
    
    answer = []    
    for i,x in enumerate(result):
        if x == max(result):
            answer.append(i+1)
            
    return answer