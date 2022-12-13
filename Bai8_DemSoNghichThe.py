
IT = [0] * 400005
ans = 0

def update(id, l, r, x):
    global IT
    global ans
    IT[id] += 1
    if l == r:
        return
    mid = (l + r)//2
    if x <= mid:
        ans += IT[id * 2 + 1]
        update(id * 2, l, mid, x)
    else:
        update(id * 2 + 1, mid + 1, r, x)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    for i in a:
        update(1, 1, n, i)

    print(ans)