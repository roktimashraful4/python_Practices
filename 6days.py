# file read write operation
# using open()

#===== read file ==== 
# file = open('note.txt') # by default r
# lekha = file.read()
# print(lekha)
# file.close()

#====== write =======

# file2 = open('note.txt','w')  # write file 
# file2.write("There are some txt")
# file2.close()


# file2 = open('note.txt','a')  # append text in  file 
# file2.write("\n new text two") 
# file2.close()

# file2 = open('note.txt','r+')  # write file 
# print(file2.read()) # read 
# file2.write("There are some txt er")
# file2.close()
