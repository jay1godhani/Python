import string
sentence=input("Write 'STOP' TO TERMINATE INPUT : ")

isTrue=True

while isTrue:
    temp=input(" ")
    if(temp=="STOP"):
        isTrue=False
    else:
        sentence+="\n"+temp
        
print("INPUT : \\n",sentence)

numOfChar=len(sentence)
numOfWords=sentence.count(" ")+sentence.count("\n")+1
lst=sentence.split()
cnt=0
for item in lst:
    if item.isalnum():
        cnt=cnt+1
      



print("******* Statistics *********")
print("No of Characters : ",numOfChar)
print("No of Words : ",numOfWords)
print("No of White Space : ",sentence.count(" "))
print("No Of Punctuation : ",sentence.count(string.punctuation))
print("Percentage Of Alphanumeric Characters : ",cnt/numOfChar*100," %")
