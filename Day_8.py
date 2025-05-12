# lst = []
# for x in range (1,101) :
#     if x%7 == 0 :
#         lst.append(x)
# print('Count =', len(lst))
# print(lst)

# string = input("input")
# count = 0
# for x in string :
#     if x in '0123456789' :
#         count += 1 
# print('Count digits + ', count)

# A = []
# x = 0 
# while x < 5 :
#     a = input("input")
#     A.append (a)
#     x += 1
# print('Last x = ', x)
# print(A)

# lst = []
# mystr = input("input")
# while len(mystr)>0 :
#     lst.append(mystr)
#     mystr = input("input")
# print(lst)
# print(len(lst))

A = [int(e) for e in input("input").split()]
x = 0
B = [] 
C = []
while x<len(A) :
    if A[x]>=0:
        B.append(A[x])
    else : 
        C.append(A[x])
    x += 1
print(A)
print(B)
print(C)