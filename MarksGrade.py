# Program to find Grade from the marks obtained.

# Taking input of marks of 5 subjects.
sub1 = int(input("Enter marks of the first subject: "))
sub2 = int(input("Enter marks of the second subject: "))
sub3 = int(input("Enter marks of the third subject: "))
sub4 = int(input("Enter marks of the fourth subject: "))
sub5 = int(input("Enter marks of the fifth subject: "))
print("These are the total marks obtained: " + str(sub1 + sub2 + sub3 + sub4 + sub5))
avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if (avg >= 90):
    print("Grade: A")
elif (avg >= 80 & avg < 90):
    print("Grade: B")
elif (avg >= 70 & avg < 80):
    print("Grade: C")
elif (avg >= 60 & avg < 70):
    print("Grade: D")
else:
    print("Grade: F")
