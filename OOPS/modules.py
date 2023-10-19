#every line to print
# f = open("try.text","r")
# print(f.seek(10))  #cursor pointer to start where to print
# print(f.read())
# f.close()

# f = open("try.text","r")
# print(f.read())
# print(f.tell())
# f.close()

# f=open("try.text")
# for line in f:
#     print(line,end=" ")

# with open ("try.text","r") as f:   #automation file closing
#     print(f.read())

# def file(fname):
#     with open(fname) as f:
#         contentlist = f.readlines()   #readline give in non-list and readlines gives output in list
#         print(contentlist)
# file("try.text")

#wap to find the no. of line in files
# def file(fname):
#     with open(fname) as f:
#         lines = len(f.readlines())
#         print(lines)
# file("try.text")

# def file(fname):
#     with open(fname) as f:
#         for i,l in enumerate(f):
#             pass
#     return i+l
# print(file("try.text"))

#wap to find the no. of count in files
# from collections import Counter
# def file(fname):
#     with open(fname) as f:
#         words = Counter(f.read().split())
#         print(words)
# file("try-1")