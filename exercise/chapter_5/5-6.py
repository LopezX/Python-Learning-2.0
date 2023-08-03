# Stages of Life
#   Write a if-elif-else chain that determines a person's stage of life:
#       - If less than 2 years, they are a toddler
#       - If at least 2 years buy less than 4 years, toddler
#       - If at least 4 years but less than 13 years, kid
#       - If at least 13 years but less than 20 years, teenager
#       - If at least 20 years but less than 65 years, adult
#       - If 65 years or older, elder
age = 20

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
elif age >= 65:
    print("You are an elder.")
    