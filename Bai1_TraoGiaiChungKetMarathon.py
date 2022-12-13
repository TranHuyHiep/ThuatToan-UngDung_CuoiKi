DDT = []
other = []

for i in range(int(input())):
    s = input().rsplit(' ', 2)
    if s[2] == 'DDT':
        DDT.append((s[0], int(s[1])))
    else:
        other.append((s[0], int(s[1])))

DDT.sort(key = lambda x:x[1], reverse = True)
other.sort(key = lambda x:x[1], reverse = True)

print("Giai nhat :%s"%DDT[0][0])
print("Giai nhi :%s"%DDT[1][0])
print("Giai ba :%s"%DDT[2][0])
print("Giai giao luu :%s"%other[0][0])
