f=open("D:\\data\\funny2.txt","r")
# f.write("\ni love php \nilove swift")
# print(f.read())
for line in f:
    tokens=line.split(' ')
    print(len(tokens))
f.close()