COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE": "7fffd4",
           "BEIGE": "#f5f5dc", "BLACK": "#000000", "BLUE": "#0000ff", "BROWN": "#a52a2a",
           "CHARTREUSE": "#7fff00", "CHOCOLATE": "#d2691e", "CORAL": "#ff7f50"}


colour = input("Enter a colour: ").upper()
while colour != "":
    if colour in COLOURS:
        print(colour, "is", COLOURS[colour])
    else:
        print("Invalid short state")
    colour = input("Enter a colour: ").upper()
