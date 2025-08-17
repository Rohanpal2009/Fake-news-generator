import random

subjects = [
    "Local man",
    "Woman in town",
    "Famous singer",
    "Group of students",
    "Auto Rickshaw driver from Delhi"
]

actions = [
    "launches",
    "dances with",
    "eats",
    "declares war on",
    "celebrates"
]

places_or_things = [
    "aliens",
    "the local train",
    "world record",
    "flying pig at park",
    "drone strike"
]

# start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n", headline)

    user_input = input("Do you want another headline? (yes/no)? ").strip().lower()
    if user_input == "no":
        break

print("Thanks for using the Fake news Generator. Have a fun day :)")