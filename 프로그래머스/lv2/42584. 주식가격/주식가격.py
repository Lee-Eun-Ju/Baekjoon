# prices 초 단위로 기록된 주식가격
# 가격이 떨어지지 않은 기간은 몇 초인가?

def solution(prices):
    from collections import deque
    prices = deque(prices)
    
    answer = []
    while prices:
        
        p = prices.popleft()     
        if not prices:
            answer.append(0)
            
        else:
            for i,x in enumerate(prices):
                if x>=p and i==len(prices)-1:
                    answer.append(i+1)
                elif x>=p:
                    pass    
                else:
                    answer.append(i+1)
                    break

    return answer