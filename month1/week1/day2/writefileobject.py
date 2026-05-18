# with open("text2.txt",'w') as f:
#     f.write("i am riddhi")
#     f.seek(0)
#     f.write("hi")

# with open('text.txt','r') as rf:
#     with open('text2.txt','w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('image.jpg','rb') as rf:
#     with open('image_copy.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('image.jpg','rb') as rf:
    with open('image_copy.jpg','wb') as wf:
        chunk_size = 4099
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



