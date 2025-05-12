A = [float(e) for e in input().split()]
B = []
x = 0
while len(B)<5 :
    if x<len(A):
        a = A[x]
    else :
        break
    x += 1
    if a<0 :
        continue
    B.append(a)
else :
    print('list B is complete')
print(B)