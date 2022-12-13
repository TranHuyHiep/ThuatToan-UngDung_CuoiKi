from collections import Counter

def BackTrack(ans, d, D, s):
    if len(ans) == len(s):
        print(ans)
        return
    for i in d:
        if D[i] > 0:
            D[i] -= 1
            BackTrack(ans + i, d, D, s)
            D[i] += 1

if __name__ == '__main__':
    s = input()
    D = Counter(s)
    d = sorted(D)
    BackTrack("", d, D, s)