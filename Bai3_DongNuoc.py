import queue

def BFS():
    n, m, k = list(map(int, input().split()))
    M = {}
    Q = queue.Queue()

    Q.put([0, 0])
    M[(0, 0)] = 0
    while Q.qsize():
        a, b = Q.get()
        c = a + b
        S = [(a, 0), (0, b), (a, m), (n, b),
             (max(0, c-m), min(m, c)), (min(c, n), max(0, c-n))]
        for s in S:
            if s not in M.keys():
                M[s] = M[(a, b)] + 1
                Q.put(s)
                if s[0] == k or s[1] == k:
                    print(M[s])
                    return
    print("Khong dong duoc nuoc")



if __name__ == '__main__':
    BFS()