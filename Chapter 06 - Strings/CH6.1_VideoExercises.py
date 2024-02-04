#Looking Inside Strings
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x-1]
print(w)

#Strings having length
print(len(fruit))

#Looping Through Strings
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print(letter)

#Using "in" as a logical operator 
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print("Found it!")