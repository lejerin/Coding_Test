import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        fm = heapq.heappop(scoville)
        if fm >= K:
            break
        if len(scoville) == 0:
            return -1
        sm = heapq.heappop(scoville)
        heapq.heappush(scoville, fm + sm*2)
        answer += 1  

    return answer
