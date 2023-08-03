#define a dictionary
alien_o = {}

print(alien_o)

#adding to the dictionary
alien_o['color'] = 'green'
alien_o['points'] = 5

#extracting the data from the dictionary
print(alien_o['color'])
print(alien_o['points'])

new_points = alien_o['points']
print(f"You just earned {new_points} points!\n")

print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

print(f"\nThe alien is {alien_o['color']}.")

#Modifying values in a dictionary
alien_o['color'] = 'yellow'
print(f"The alien is now {alien_o['color']}.")

#Removing values from a dictionary
del alien_o['points']

print(alien_o)
