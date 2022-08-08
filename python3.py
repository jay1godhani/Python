f=open("jay1.txt","r")
count =0
for i in f:
    if i[0]!='J':
        count+=1

print(count)
