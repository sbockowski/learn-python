# Decoupling is simply the process of splittining or dividing the responsibilities of a function
feet_inches = input("Enter feet and inches")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return feet, inches

def convert(feet, inches):

    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters
f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")

# password = "Upersasda"

# for letter in set(password):
#     if letter.isupper:
#         pass_upper = True
