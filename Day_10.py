# m = 5
# n = 3 
# for x in range(m):
#     print(x, end=':')
#     for y in range(n):
#         print(str(x)+str(y), end= ' ')
#     print()


# n = int ( input())
# while n>0 :
#     for x in range (1,n+1):
#         if n%x == 0:
#             print(x, end=' ')
#     print()
#     n = int ( input() )


# n = int( input('n='))
# for x in range(n):
#     for y in range (n):
#         print('*',end=' ')
#     print()


y =  [ 25, 12, 31, 16, 12 ]
x =  int( input('x = ') )
index = 0
found = -1 
while index < len(y) :
    a = y[index]
    if a== x:
        print(a, 'is found at ',index)
        found = index 
    index += 1
if found == -1 :
    print(x, 'is not found')

