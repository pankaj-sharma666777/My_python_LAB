x=input("enter 1st number: ")
y=input("enter 2nd number: ")
try:
    z=int(x)/int(y)
except Exception as e:
    print("exeption occured: ",e)
    z=None
print("devision is: ", z)        