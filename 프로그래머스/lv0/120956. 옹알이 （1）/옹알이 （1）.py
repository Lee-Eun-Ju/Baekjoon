import itertools
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	

def solution(babbling):
    answer = 0
    w = ["aya", "ye", "woo", "ma"]
    
    data = []
    for i in range(len(w)+1):
        x =list(itertools.permutations(w,i))
        for j in range(len(x)):
            data.append("".join(x[j]))
        
    for b in babbling:
        if b in data:
            answer +=1
    return answer

result = solution(babbling)
print(result)