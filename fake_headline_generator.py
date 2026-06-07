# 1- import the random module
import random
# 2- Create subjects
subjects = [
    "Eagle",
    "Waseem Akram",
    "Lion",
    "A group of monkeys",
    "Karachi Zoo",
    "Shahi Qila Lahore",
    "Tiger",
    "Car driver from Faisalabad",
    "Prime Minister of Pakistan",
    "Safari Park Islamabad"
]

actions = [
    "flies",
    "runs",
    "jumps",
    "swims",
    "climbs",
    "dances",
    "sings",
    "plays",
    "works",
    "travels"
]

places_or_things = [
    "in the sky",
    "on the ground",
    "in the water",
    "on the tree",
    "in the city",
    "at the zoo",
    "in the park",
    "on the road",
    "in the office",
    "at home"
]

# 3- Creating loop for generating random headlines
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"{subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break
# 4- Print Thank you message
    print("\nThanks for using the Fake News Headline Generator! Goodbye!")