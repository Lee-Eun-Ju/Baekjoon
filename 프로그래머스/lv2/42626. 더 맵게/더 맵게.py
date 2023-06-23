def solution(scoville, K):
    from heapq import heappop, heappush, heapify
    heapify(scoville) 
    
    answer = 0
    while True:
        
        first = heappop(scoville)
        if first >= K:
            break
        if not scoville and first<K:
            answer = -1
            break
            
        second = heappop(scoville)
        heappush(scoville, first +(second*2))
        answer += 1    
    
    return answer