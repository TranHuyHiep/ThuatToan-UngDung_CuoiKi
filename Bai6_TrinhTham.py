import queue

Q = queue.PriorityQueue()
n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    Q.put([-a[i], i])
    if Q.qsize() >= k:
        while Q.queue[0][1] <= i - k:
            Q.get()
        print(-Q.queue[0][0], end=" ")
