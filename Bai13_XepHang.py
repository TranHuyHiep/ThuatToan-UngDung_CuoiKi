import queue

n = int(input())
a = list(map(int, input().split()))
st = queue.LifoQueue()

res = 0
st.put([2e9, 0])
for i in range(n):
    while st.queue[-1][0] < a[i]:
        res += st.get()[1]
    if st.queue[-1][0] == a[i]:
        res += st.queue[-1][1] + (st.queue[-2][1] != 0)
        st.queue[-1][1] += 1
    else:
        res += (st.queue[-1][1] != 0)
        st.put([a[i], 1])
print(res)
