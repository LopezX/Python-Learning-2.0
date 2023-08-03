# Glossary 2
#   Clean up the code from Glossary and instead loop through the dictionary. Add
#   5 more items to the dictionary.
glossary = {
    'key':'a specific word or phrase that accesses a value when called',
    'dictionary':'a list of key-value pairs, where the value is accessed when the key is called',
    'list':'an array of elements that can be accessed by calling its index',
    'for-loop':'a type of loop that goes for a set amount of iterations',
    'object':'a data type that is created to store multiple data types with itself',
    'get()':'Checks to see if a key is associated to a value, else it print "None" or a given value',
    'sorted()':'sorts the list, set, etc. in alphabetical or numerical order',
    'set()':'takes a list and makes it into a set, which has no repeating values',
    'conditions':'A statement that must be true or false in order for something to occur',
    'title()':'Capitalizes the first letter of each word in the string',
}

for term, definition in glossary.items():
    print(f"{term.title()}:")
    print(f"{definition}\n")
    