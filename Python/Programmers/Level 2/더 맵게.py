import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K:
        if len(scoville)==2 and scoville[0]+(scoville[1]*2)<K:
            return -1
        else:
            m_sco=heapq.heappop(scoville)
            m2_sco=heapq.heappop(scoville)
            heapq.heappush(scoville,m_sco+(m2_sco*2))
            answer+=1
    return answer

# (정확성은 통과하지만 효율성은 통과 x)
def solution(scoville, K):
    scoville=sorted(scoville)
    answer = 0
    while min(scoville)<K:
        if len(scoville)==2 and scoville[0]+(scoville[1]*2)<K:
            return -1
        else:
            m_sco=scoville.pop(scoville.index(min(scoville)))
            m2_sco=scoville.pop(scoville.index(min(scoville)))
            scoville.insert(0,m_sco+(m2_sco*2))
            answer+=1
    return answer
