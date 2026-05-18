with open('text.txt','r') as f: # does not need to explicitly close the file
    # print(f.read())
    # f_contents=f.read()
    # f_contents1=f.readlines()
    # print(f_contents1)
    # print(f_contents)
    # f_contents1=f.readline() prints one line for single piecee of code
    # print(f_contents1)
    # for line in f:
    #     print(line,end="")
    # f_content=f.read(50) prints specific amount according to size
    # print(f_content)

    # size_to_read = 20
    # f_content=f.read(size_to_read )
    # while len(f_content)>0:
    #     print(f_content,end = " @ ")
    #     f_content=f.read(size_to_read )
    # print(f.tell())

    size_to_read = 10
    f_contents= f.read(size_to_read)
    print(f_contents)
    f.seek(5)
    f_contents= f.read(size_to_read)
    print(f_contents)




# f = open('text.txt','r')
# print(f.name)
# print(f.mode)
# f.close()
# print(f.closed)