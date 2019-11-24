
import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    count = 0

    while len(heap)>0:


        if heap[0] >= K:
            return count
        a = heapq.heappop(heap)
        if heap != []:
            # print('여길와야지')
            b = heapq.heappop(heap)
            heapq.heappush(heap, a +(b*2))
        count += 1
        # print(count)

    return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
