Question = input("Harry Potter or Stranger Things? ").lower()
if Question == "harry potter":
    answer1 = input("Who is Harry Potter's godfather? ").lower()
    if answer1 != "sirius black":
        print("SIRIUS-ly? That's like... fan 101.")
    elif answer1 == "sirius black":
        answer2 = input("What house was Luna Lovegood in? ").lower()
        if answer2 != "ravenclaw":
            print("You're giving very movie-only energy right now.")
        elif answer2 == "ravenclaw":
            answer3 = input("What's the spell to disarm your opponent? ").lower()
            if answer3 != "expelliarmus":
                print("You clearly would not last five minutes in a duel.")
            elif answer3 == "expelliarmus":
                print("HELLO, Fellow Harry Potter fan!")
elif Question == "stranger things":
    answer1 = input("What's the name of the Dungeons & Dragons monster from Season 1? ").lower()
    if answer1 != "demogorgon":
        print("Wrong already? Eddie Munson is disappointed in you.")
    elif answer1 == "demogorgon":
        answer2 = input("Who was the first character taken to the Upside Down? ").lower()
        if answer2 != "will":
            print("You sure you're not mixing this up with Narnia?")
        elif answer2 == "will":
            answer3 = input("What song saved Max from Vecna? ").lower()
            if answer3 != "running up that hill":
                print("You're not a real fan until you've cried to that song at least once.")
            elif answer3 == "running up that hill":
                print("HELLO, Fellow Stranger Things fan!")
else:
    print("Hmm, I don't have that fandom loaded yet. Try 'Stranger Things' or 'Harry Potter' to unlock maximum judgment.")