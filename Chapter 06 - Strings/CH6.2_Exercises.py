fruit = 'banana'
#Using "in" as a logical operator 
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print("Found it!")

#String Library ".lower()"
#do not modify the original string but return a new string that has been altered 
greet = 'Hello Bob'
zap = greet.lower()
print(zap) #makes it lower case letter
print(greet) #Capitalizez first letter of each word
print("Hi There". lower()) #makes it lower case letter

#String Library ".upper()"
nnn = greet.upper() #makes every letter uppercase 
print(nnn)

#Searching a string ".find()"
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)