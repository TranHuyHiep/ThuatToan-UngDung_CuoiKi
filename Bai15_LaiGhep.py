
def BackTrack(ans, s1, s2):
    if len(ans) == len(s1):
        print(ans)
        return
    i = len(ans)
    a, b = s1[i], s2[i]
    if a > b: a, b = b, a
    BackTrack(ans + a, s1, s2)
    if a != b: BackTrack(ans + b, s1, s2)

if __name__ == '__main__':
    s1 = input()
    s2 = input()

    BackTrack("", s1, s2)
