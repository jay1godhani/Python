f = open ("jay1.txt","r")
count=0
for i in f:
    for j in i:
        if(j.isupper ()):
            count+=1

print(count)
