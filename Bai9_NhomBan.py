F = [0] * 10005
P = [1] * 10005

def root(x):
    if F[x] == 0:
        return x
    return root(F[x])

if __name__ == '__main__':
    n, m = map(int, input().split())
    res = n
    Max = 1
    for i in range(m):
        u, v = map(int, input().split())
        a = root(u)
        b = root(v)

        if a != b:
            if P[a] <= P[b]: a, b = b, a
            F[b] = a
            P[a] += P[b]
            res -= 1
        Max = max(Max, P[a])
    print(res)
    print(Max)