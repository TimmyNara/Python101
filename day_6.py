# score = float(input("put score"))
# if score%1 >= 0.8 :
#     score += 1
# score = int(score)
# print(score)
# hr = int(input("put hour"))
# day = hr//12
# if hr%12 >= 10 :
#     day += 1
# print(day)
# a =  input("put number")
# if a.isnumeric() :
#     a = int(a)

# print(a, type(a))
# a,b,c = input().split()
# a=int(a)
# b=int(b)
# c=int(c)
# if a<b+c and b<a+c and c<a+b :
#     print("triangle")
# else :
#     print("not triangle")
# midterm, final = input("put score midterm and final").split()
# mt = float(midterm)
# fn = float(final)
# sm = mt+fn
# print(sm)
# if sm <= 50 :
#     print("fail")
# else :
#     if mt<15 :
#         print("fail")
#     else :
#         if fn<15 :
#             print("fail")
#         else :
#             print("Pass")
# s = float(input())
# if s >= 80.0 :
#     grade='a'
# elif s >= 60.0 :
#     grade='b'
# elif s >= 50.0 :
#     grade='c'
# elif s >= 40.0 :
#     grade='E'
# print(grade)
n = int(input())
if n == 0 :
    result="Zero"
else :
    if n > 0 :
        result = "Positive"
    else :
        result = "negative"
    if n%2 == 0 :
        result += "even number"
    else :
        result += "odd number"
print(result)
