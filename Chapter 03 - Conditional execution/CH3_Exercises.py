'''Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

en_hrs = float(input("Enter Hours:"))
en_rate = float(input("Enter Rate:"))

if en_hrs > 40:
    pay = (en_hrs - 40) * (en_rate  * 1.5) + (40 * en_rate)
    print("Overtime: $",pay)
else:
    pay = en_hrs * en_rate
    print('Regular: $',pay)

'''Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''

try: 
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter rate: "))
except:
    print ("Error, please enter numeric input!")
    quit()


while True:
    try: 
        en_score = float(input('Enter score: '))
        break
    except ValueError:
        print("Bad Score!")

if en_score < 0 or en_score > 1.0:
    print("Please enter the correct score")
elif en_score >= 0.9:
    print("Score: A")
elif en_score >= 0.8: 
    print("Score: B")
elif en_score >= 0.7:
    print("Score: C")
elif en_score >= 0.6:
    print("Score: D")
else: 
    print("Score: F")

