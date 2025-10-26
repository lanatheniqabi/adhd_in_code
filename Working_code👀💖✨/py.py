ask = input("what is your name? ")
print("hello,", ask)
ask2 = input("what is the reason for your visit? ")
if ask2 == "regular checkup":
    print("the OPD is to the left")
elif ask2 == "emergency":
    print("the ER is to the right")
else:
    print("fill this form out and we'll see")

            