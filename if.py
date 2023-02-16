#if statement
x=1
marks=49
grade=24
days=98
if(x>0):
    print("The number is positive")
#if... else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed the Exam")
#if.. elif.. else statement
if(grade<=29 and grade>=0):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distiction")
else:
    print("Wrong grade entered")
if(days<=7 and days>=0):
    print("Week")
elif days>=8 and days<=14:
    print("a fortnight")
elif days>=14 and days<=21:
    print("Month")
elif days>=22 and days<=90:
    print("a quarter year")
elif days>=91 and days<=180:
    print("a half a year")
elif days>=181 and days<=365:
    print("a year")
else:
    print("Wrong days entered")