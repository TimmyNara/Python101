# import math

# print(F'{math.e:.2f}')
# print(F'{math.exp(2):.2f}')
# print(F'{math.fabs(-10.5)}')
# print(F'{math.log(7.39):.2f}')


# print(F'{math.sin(math.pi/6):.2f}')
# print(F'{math.cos(math.pi/6):.2f}')
# print(F'{math.tan(math.pi/6):.5f}')
# print(F'{math.asin(0.50):.2f}')
# print(F'{math.acos(0.87):.2f}')
# print(F'{math.atan(0.57735):.2f}')
# print(F'{math.degrees(math.pi/6):.2f}')
# print(F'{math.radians(30):.2f}')


# import random
# print(F'{random.random():.2f}')
# print(random.randint(1,9))
# sequence = ["apple", "bannana", "coconut"]
# random.shuffle(sequence)
# print(sequence)

# random.seed(10)
# print(F'{random.random():.2f}')
# print(random.randint(1,9))


# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%c"))
# date_format = "%d-%m-%Y"
# print(x.strftime(date_format))

# datetime_format = "%a %d %B %Y %H:%M:%S"
# print(x.strftime(datetime_format))


# import pathlib
# path = pathlib.Path("test.txt")
# print(path.exists())
# path2 = pathlib.Path("d:/pytest/hello/txt")
# print(path2.exists())


# f = open("test.txt", "r")
# print(f.read(5))

# f = open("test.txt", "r")
# print(f.read())


# f = open("test.txt", "r")
# print(f.readline())

# f = open("test.txt", "r")
# print(f.readline())
# print(f.readline())


# f = open("test.txt", "r")

# for x in f:
#     print(x)


f = open("test.txt", "r")
print(f.readlines())