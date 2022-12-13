import queue, math

n = int(input())
Q = queue.Queue()
M = {}
ans = []

Q.put(n)
while Q.qsize():
    x = Q.get()
    ans.append(x)

    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            t = (i - 1) * (x//i + 1)
            if t not in M.keys():
                M[t] = 1
                Q.put(t)
ans.sort()
print(*ans)