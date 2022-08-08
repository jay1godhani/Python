def addname1(name):
    f=open("jay1.txt","a")
    f.write(name+"\n")
    f.close()
def fstudent(name):
    f=open("jay1.txt","r")
    flag=0;
    for i in f:
        c=name+"\n"
        if i==c:
            print(name+" found")
            flag=1
        if flag==0:
            print(name+"is not found")

f=open("jay1.txt","a")
addname1("JAY")
addname1("ALAY")
addname1("DARSHIT")
addname1("CHAMAN")
addname1("PIYUSH")
addname1("PRINCE")

fstudent("JAY")

