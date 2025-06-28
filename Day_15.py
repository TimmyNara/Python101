# f = open("test.txt", "a")                    #a is add more content
# f.write("Now the file has more content!")
# f.close()

# f = open("test.txt", "w")                    #w is rewriting the content
# f.write("Now the file has more content")
# f.close()


# f= open("test.txt", "a")
# f.writelines({"\n see you a soon!", "ove and out."})
# f.close()

# f = open("test.txt", "r")
# print(f.read())


import os

# if os.path.exists("Test.txt"):
#     os.remove("Test.txt")
# else:
#     print("the file does not exists")


# with open('test.txt', 'r') as fhandler:
#     data = fhandler.read()
#     print(data)

# with open('test.txt', 'w') as fhandler:
#     fhandler.write("Hello World")


# try:
#     fin = open('test.txt')
#     for line in fin:
#         print(line)
#     fin.close()
# except :
#     print('Somthing went wrong')


# try:
#     with open('test.txt', 'r') as fhandler:
#         data = fhandler.read()
#         print(data)
# except IOError as ex:
#     print("Error perfoeming I/O operations on file:", ex)


# try:
#     with open('bad_file', "w") as fhandler:
#         fhandler.write('hello world')
# except IOError as ex:
#     print("Error performing I/O operations on file:", ex)