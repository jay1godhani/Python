def convertFeetToInches(feet):
    return feet*12
def takeInput():
    number=float(input("Enter Your Value in Feet : "))
    return number
def printValue(feet,inch):
    print(feet," feet = ",inch," inch")
    
feet=takeInput()
inch=convertFeetToInches(feet)
printValue(feet,inch)
