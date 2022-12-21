n=input()
sumOfNumber=0
productOfNumber=1
for i in n:
    sumOfNumber+=int(i)
    productOfNumber*=int(i)
print(productOfNumber-sumOfNumber)