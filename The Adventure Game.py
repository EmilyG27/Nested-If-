# Task 1
place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river?")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
# Task 2
elif place == "cave":
    cave_action = (input("Would you like to light a torch or proceed in the dark?"))
    if cave_action == "light a torch":
        print("The cave lights up and you can see the way forward.")
    else:
        print("You can't see anything but you can hear something in the distance.")
#Task 3
else:
    pass