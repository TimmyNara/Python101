# a = {5,4,3,2,2,3,7,8,9,1}
# print(type(a))
# print(a)
# print(len(a))
# s2 = set("hello")
# print(s2&{"w","e"})
# print(s2|{"l","o"})
# s2.add(3)
# s2.remove("l")
# s2.pop()
# print(s2)
# s3 = {"name":"Nara",
#     "surname":"Sipa",
#     "age": 12,
#     "nickname": "Timmy"}
# print(s3)
# print(s3["name"])
# print(s3["nickname"])
# s3["age"] = 15
# print(s3)
# print(len(s3))
n = int(input('enter your Number'))
if n>0 :
    if n%2 == 0 :
        print('Even Positive Number')
    else :
        print('Odd Positive Number')
else :
    if n%2 == 0 :
        print('Even negative Number')
    else :
        print('Odd Negative Number')