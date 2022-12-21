s=input()
uniqueCharacter=False
for i in s:
    if s.count(i)==1:
        print(i)
        uniqueCharacter=True
        break
if uniqueCharacter==False:
    print('-1')