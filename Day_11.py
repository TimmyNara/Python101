# y = [ (64125,2.15), (64104, 2.87), (64402, 3.54),
#      (64110, 3.15), (64500, 2.05), (64064, 2.64) ]
# x = int( input ('x = '))

# found = -1
# index = 0
# while index < len(y) :
#     a = y[index]
#     if a [0] == x :
#         print('GPA of ', x,' = ',a[1])
#         found = index
#         break
#     index += 1
# if found == -1 :
#     print(x, 'is not found')


 
y = [22, 25, 12, 75, 12, 65]
x = 65
found = -1
left = 0 
right = len(y)
z = y[left:right]
while len(z)>0 :
    m = (left+right)//2
    if y[m] == x :
        found = m 
        break
    elif x >y [m] :
        left=m+1
        z = y [left:right]
    else : 
        right = m
        z = y[left:right]
if found == -1 :
    print(x,' is not found')
else :
    print(x, 'is found at', found)
