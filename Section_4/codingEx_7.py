#This exercise extracts all the capitals from the quotes 

Quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water, and Public Health, What have the Romans ever done to us?"

Quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water system, and Public Health, What have the Romans ever done to us?"

Quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done to us?"


for character in Quote:
    if character.isupper():
        print(character);