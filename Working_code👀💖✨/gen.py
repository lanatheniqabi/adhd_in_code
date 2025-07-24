# ask the user for their birth year
birthYear = int(input("What year were you born in? "))

# check which generation they belong to, based on rough cutoffs
if birthYear <= 1945:
    # born before 1946 – Traditionalist generation
    print("You're a Traditionalist. The world was quieter then, but the silence carried weight.")
elif birthYear <= 1964:
    # 1946 to 1964 – Baby Boomers
    print("You're a Baby Boomer. Born into the aftershocks of war, you witnessed the world shift and tried to shape it.")
elif birthYear <= 1980:
    # 1965 to 1980 – Generation X
    print("You're Gen X. The forgotten middle child of generations. Self-reliant, sharp, and often underestimated.")
elif birthYear <= 1996:
    # 1981 to 1996 – Millennials
    print("You're a Millennial. Raised between analog and digital, always adapting, always searching for meaning.")
elif birthYear <= 2012:
    # 1997 to 2012 – Generation Z
    print("You're Gen Z. You didn't choose the chaos, but you learned to breathe in it. Hyper-aware, hungry for truth.")
else:
    # 2013 and onward – Generation Alpha
    print("You're Gen Alpha. Just getting started. You are the question mark at the end of the sentence the rest of us wrote.")
