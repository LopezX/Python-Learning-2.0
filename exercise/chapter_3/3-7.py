# Shrinking Guest List:
#   With the program from 3-6 (copied here), add a print call saying your table
#   won't arrive on time. Use pop to remove people from the list until two are 
#   left. Tell the people they are still welcome to come, then use 'del' to 
#   remove the last two from the list, printing the list at the end to ensure
#   the list is empty.
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

print("\nI can only invite two to dinner tonight.\n")

print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")
print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")
print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")
print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")
print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")
print(f"I'm sorry, but I can't invite you, {guest_names.pop().title()}, to dinner tonight.")

print(f"You are still invited to dinner tonight, {guest_names[0].title()}")
print(f"You are still invited to dinner tonight, {guest_names[1].title()}")

del guest_names[1]
del guest_names[0]

print(guest_names)
