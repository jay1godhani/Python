f=open("jay1.txt","r")
count =0
for i in f:
    count+=1
    for j in i:
        if j==" ":
            count+=1

print(count)
