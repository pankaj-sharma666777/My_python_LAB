f=open("D:\\data\\funny2.txt","r")
f_out=open("D:\\data\\funny_wca.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write("wordcount:"+str(len(tokens))+line)

f.close()
f_out.close()    