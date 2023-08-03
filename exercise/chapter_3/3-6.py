# More Guests:
#   With the program from 3-4 or 3-5 (copied here), add a print call saying you
#   found a bigger dinner table. Insert one guest in the beginning, one in the 
#   middle, and one at the end of your list. Print a new set of invitations.
guest_names = ['george washington', 'johnny depp', 'kobe bryant', 'john cena', 'ryan reynolds']

print(f"I would like to invite you, {guest_names[0].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[1].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[2].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[3].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[4].title()}, to dinner tonight!")

print(f"\n{guest_names[3].title()} can't make it to dinner tonight.\n")
guest_names[3] = 'elon musk'

print(f"I would like to invite you, {guest_names[0].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[1].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[2].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[3].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[4].title()}, to dinner tonight!")

print("\nI found a bigger table for dinner tonight.\n")

guest_names.insert(0, 'Dwayne Johnson')
guest_names.insert(3, 'Seth Rogen')
guest_names.append('Gabriel Gonzalez')

print(f"I would like to invite you, {guest_names[0].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[1].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[2].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[3].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[4].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[5].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[6].title()}, to dinner tonight!")
print(f"I would like to invite you, {guest_names[7].title()}, to dinner tonight!")
