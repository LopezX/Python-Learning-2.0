# Changing Guest List:
#   With the program from 3-4 (copied here), add a print call for somebody that
#   couldn't make it. Replace that person in the list with somebody else. Send 
#   a second set of invitiation messages for each person still in the list.
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
