ask = input("how are you feeling right now? ").strip().lower()
if ask == "good":
    print("say Alhamdulillah!")
elif ask == "not the best":
    print("better is on the way...")
elif ask == "bad":
    print("you'll figure it out, you always do.")
elif ask == "nothing":
    print("shouldn't you be feeling something?")
else:
    print("out of order, hehe")