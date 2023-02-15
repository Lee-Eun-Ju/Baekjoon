dots = [[1, 4], [9, 2], [3, 8], [11, 6]]

def lam(x,y):
        result = (x[1]-y[1])/(x[0]-y[0])
        return result
    
def solution(dots):
    answer = 0
    
    data = []
    data.append([lam(dots[0],dots[1]), lam(dots[2],dots[3])])
    data.append([lam(dots[0],dots[2]), lam(dots[1],dots[3])])
    data.append([lam(dots[0],dots[3]), lam(dots[1],dots[2])])
  
    for i in data:
        if i[0]==i[1]:
            answer =1                        
    return answer
    
print(solution(dots))