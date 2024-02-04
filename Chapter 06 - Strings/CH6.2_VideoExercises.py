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

#Search & Replace ".replace()"
#replaces all occurences of the search string with the replacement string 
nstr = greet.replace('Bob', 'Jane')
print(nstr)

abc = greet.replace('o', 'x')
print(abc)

#Stripping whitespace
#.lstrip() - removes whitespace at the left 
greeting = " Hello Bob "
greeting.lstrip()
#.rstrip() - removes whitespace at the right
greeting.rstrip()
#.strip() - removed both beginning and ending whitespace 
greeting.strip()

#Parsing & Extracting
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
