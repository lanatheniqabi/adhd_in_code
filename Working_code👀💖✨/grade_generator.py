testName =  input("What is the name of the test?: ")
maxMarks = input("What are the maximum marks?: ")
obtMarks = input("How many marks did you obtain?: ")
obtMarks = int(obtMarks)
maxMarks = int(maxMarks)
percentage = obtMarks / maxMarks * 100 
if percentage <= 90:
    print("Your grade is A+!")
elif percentage <= 80:
    print("Your grade is A!")
elif percentage <= 70:
    print("Your grade is B!")
elif percentage <= 60:
    print("Your grade is C!")
elif percentage <= 50:
    print("Your grade is D!")
elif percentage <= 40:
    print("Your grade is F!")
