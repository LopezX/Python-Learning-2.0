# Stripping Names;
#   Use a vairable to represent a person's name, and include whitespace at the
#   beginning and the end of the name (use characters such as \t and \n at
#   least once). Print the name with whitespace, then with the three stripping
#   functions lstrip(), rstrip(), and strip()
name = '   \t   \n  Nathan\n\n\t   \t     '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
