def main():
    name = input("what's your name? ")
    mood = input("how are you feeling today? ")
    tell(name,mood)

    tell(name, mood)

def tell(to="friend", mood="okay"):
    print("hello,", to)
    print("Oh, you're feeling", mood + "?")
    print("Say Alhamdulillah.")  

main()


   