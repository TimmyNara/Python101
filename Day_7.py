# H,M = input("inter your hour and minute").split(':')
# H = int(H)
# M = int(M)
# if (M>=30) :
#     H+= 1
# if H<=6 :
#     p = H*100
# elif H<= 10 :
#     p = 6*100(H-6)*125
# elif H<=15 :
#     p=6*100+4*125+(H-10)*150
# else :
#     p=6*100+4*125+5*150
# print('Payment =',p, 'baht')
# x = input("put word")
# vowels = {'a','e','i','o','u','A','E','I','O','U'}
# if (x[0] in vowels) :
#     print(x, 'begins with a vowel.')
# else :
#     print(x, 'does not begin with a vowel.')
# A = [3, 4, 8, 6, 1]
# for e in A :
#     print(e)
# A = [3, 4, 8, 6, 1]
# N = len(A)
# for x in range(N-1,-1,-1) :
#     print(A[x])
A = [3, 4, 8, 6, 1]
N = len(A)
s = ''
print(A[0])
for x in range(-1,-N-1,-1) :
    s += str(A[x])+'  '
print(s)
