# Affirmations according to the day of the week
Name = input("What should I call you today? ")
DOF = input("Which day has dawned on your horizon? ").lower()
if DOF == "monday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Let Monday fall soft as rain—you rise quietly, gently, full of grace.")
    elif Fav == "books":
        print("You turn the page of Monday like a whispered spell. You are your own plot twist.")
    else:
        print("You carry Monday with the quiet power of", (Fav), "—steady, strong, and entirely yours.")
elif DOF == "tuesday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Tuesday drizzles, but you move through it like a rhythm—calm, constant, beautiful.")
    elif Fav == "books":
        print("Each chapter of Tuesday opens with your name—curious, unfolding, full of light.")
    else:
        print("Like", (Fav), "you brighten Tuesday in a way only you can.")
elif DOF == "wednesday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Midweek rains bring clarity—you are soft thunder and clear skies at once.")
    elif Fav == "books":
        print("Let Wednesday read like a comfort story—familiar, loved, and full of heart.")
    else:
        print("Wednesday echoes your love for", (Fav), "—it steadies you, quietly and fully.")
elif DOF == "thursday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Thursday rolls in heavy, but you are the stillness after the storm.")
    elif Fav == "books":
        print("You edit Thursday like prose—intentional, precise, quietly bold.")
    else:
        print("Thursday listens when you speak in the language of", (Fav), ".")
elif DOF == "friday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Let the rain tap its rhythm—you're dancing through Friday like soft thunder.")
    elif Fav == "books":
        print("You close the chapter of the week with grace—Friday belongs to the storyteller in you.")
    else:
        print("You shine through Friday like", (Fav), "in full bloom.")
elif DOF == "saturday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Rain on Saturday is a lullaby—let it soften you into peace.")
    elif Fav == "books":
        print("You read Saturday slow, like a poem you've waited to understand.")
    else:
        print("Saturday opens like", (Fav), "—unexpected, alive, and full of wonder.")
elif DOF == "sunday":
    Fav = input("What's one small thing you're loving today? ").lower()
    if Fav == "rain":
        print("Sunday rain is sacred—let it wash over you and carry the week away.")
    elif Fav == "books":
        print("Let Sunday be the quiet epilogue—you've written a beautiful seven-day arc.")
    else:
        print("Sunday hums with the comfort of", (Fav), "—you've earned this stillness.")
else:
    print("Time is a lie. Please enter a real weekday.")
