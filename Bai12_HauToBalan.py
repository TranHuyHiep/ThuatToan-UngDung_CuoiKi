import queue

UT = {'(':0, '+':1, '-':1, '*':2, '/':2}

def HauToBalan(s):
    ans = ""
    st = queue.LifoQueue()
    for i in s:
        if i == '(':
            st.put(i)
        elif '0' <= i and i <= '9':
            ans += i
        elif i == ')':
            while st.qsize() and st.queue[-1] != '(':
                ans += st.get()
            st.get()
        else:
            while st.qsize() and UT[i] <= UT[st.queue[-1]]:
                ans += st.get()
            st.put(i)
    while st.qsize():
        ans += st.get()
    return ans

def tinh(s):
    st = queue.LifoQueue()
    for i in s:
        if '0' <= i and i <= '9':
            st.put(int(i))
        else:
            a = st.get()
            b = st.get()
            if i == '+': st.put(b + a)
            elif i == '-': st.put(b - a)
            elif i == '*': st.put(b * a)
            else: st.put(b // a)
    return st.get()


if __name__ == '__main__':
    s = input()

    hauto = HauToBalan(s)
    print(hauto)
    print(tinh(hauto))