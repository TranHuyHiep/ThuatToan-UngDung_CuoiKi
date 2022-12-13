A = [0] * 100005
IT = [0] * 500005

def update(id, l, r):
    if l == r:
        IT[id] = A[l]
        return
    mid = (l + r)//2
    update(2 * id, l, mid)
    update(2 * id + 1, mid + 1, r)
    IT[id] = max(IT[2 * id], IT[2 * id + 1])

def find(id, l, r, u, v):
    if v < l or r < u: return -2e9
    if u <= l and r <= v: return IT[id]
    mid = (l + r)//2
    return max(find(2 * id, l, mid, u, v), find(2 * id + 1, mid + 1, r, u, v))

if __name__ == '__main__':
    n, m = map(int, input().split())
    A[1:n+1] = list(map(int, input().split()))
    update(1, 1, n)
    for i in range(m):
        u, v = map(int, input().split())
        print(find(1, 1, n, u, v))