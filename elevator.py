import random
user_choice = random.randint(0, 20)

floor_no = input(f"Welcome! This is floor {user_choice} \n")
name = input("What is your name? ")
print("Hi " + name + " It's nice to have you here")
direction = input("Are you going up or down ")


if direction == "up":
    floor_no = input("How many floor? ")
    no_of_floor = user_choice + int(floor_no)
    print("Hold on tight, we are going up...")
    print(f"We started from floor {user_choice} and we have arrived at floor { no_of_floor} do have a nice day.")

else:
    floor_no = input("How many floors? ")
    no_of_floor = user_choice - int(floor_no)
    print("Hold on tight, we are going up...")
    print(f"We started from floor {user_choice} and we have arrived at floor{no_of_floor} do have a nice day")
