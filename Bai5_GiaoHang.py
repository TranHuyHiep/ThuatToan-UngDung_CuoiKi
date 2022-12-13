import queue

A = [[] for _ in range(10005)]
Q = queue.PriorityQueue()
ans = 0
n = int(input())
for i in range(n):
    u, v = map(int, input().split())
    A[u].append(v)

for i in range(1005, 0, -1):
    for j in A[i]: Q.put(-j)
    if Q.qsize(): ans += Q.get()

print(-ans)