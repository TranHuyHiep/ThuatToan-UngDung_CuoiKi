F = [0] * 100005
D = [1] * 100005

def root(x):
    if F[x] == 0:
        return x
    return root(F[x])

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = []
    for i in range(m):
        u, v, w = map(int, input().split())
        A.append((u, v, w))
    A.sort(key=lambda x:x[2])

    ans = 0
    for i in range(m):
        u, v, w = A[i]
        a = root(u)
        b = root(v)

        if a != b:
            if D[a] < D[b]: a, b = b, a
            F[b] = a
            D[a] += D[b]
            ans += w
    print(ans)