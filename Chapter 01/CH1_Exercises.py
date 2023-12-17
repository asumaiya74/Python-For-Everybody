"""Exercise 2: Write a program that uses input to prompt a user for their
name and then welcomes them.
Enter your name: Chuck
Hello Chuck """

'''
en_name = input("Enter your name:")
print("Hello", en_name)'''

""" Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay. 

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25 """

'''
en_hrs = input("Enter Hours:")
en_rate = input("Enter Rate:")
pay = float(en_hrs) * float(en_rate)
print("Pay: $", pay)
'''

'''Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.'''

temp = float(input("Enter temperature in celsius: "))
fah_conv = temp * 1.8 + 32
print('Fahrenheit:', fah_conv)

