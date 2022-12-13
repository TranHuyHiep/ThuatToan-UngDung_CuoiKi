import queue

step = [(-1, -1),
        (-1, 0),
        (-1, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, -1),
        (0, 1)]

def BFS():
    n, m = map(int, input().split())
    matrix = []
    q = queue.Queue()
    ans = []
    d = []

    for i in range(n):
        d.append([0] * m)
        matrix.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and d[i][j] == 0:
                q.put((i, j))
                d[i][j] = 1
                count = 1
                while q.qsize():
                    temp = q.get()
                    for s in step:
                        x = temp[0] + s[0]
                        y = temp[1] + s[1]
                        if x >= 0 and x < n and y >= 0 and y < m and d[x][y] == 0 and matrix[x][y] == 0:
                            q.put((x, y))
                            d[x][y] = 1
                            count += 1
                ans.append(count)
    ans.sort()
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    BFS()