import queue

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    QL = queue.LifoQueue()
    QR = queue.LifoQueue()
    L = []
    R = []
    ans = []

    QL.put([2e9, -1])
    for i in range(n):
        while QL.queue[-1][0] <= a[i]:
            QL.get()
        L.append(QL.queue[-1][1])
        QL.put([a[i], i])

    QR.put([2e9, -1])
    for i in range(n-1, -1, -1):
        while QR.queue[-1][0] <= a[i]:
            QR.get()
        R.append(QR.queue[-1][1])
        QR.put([a[i], i])
    R.reverse()

    for i in range(n):
        if L[i] == -1 and R[i] == -1: ans.append(-1)
        elif L[i] == -1: ans.append(R[i])
        elif R[i] == -1: ans.append(L[i])
        else:
            if i - L[i] > R[i] - i: ans.append(R[i])
            else: ans.append(L[i])
    print(*ans)