# Programmed by John Elehwany and Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 2, 2024
# Lab Assignment: 03


# DATA IN

# States names of program and asks user for input of hill type
print("""
This program calculates your ski jump and 
""")

hill_type = input(('Enter the type of hill: '))
speed = input(('Enter the speed: '))

# Value of speed, points, and par if the hill type is either normal or large. Prints the values afterward
if hill_type == 'normal':
    hill_height = 46
    hill_points = 2
    hill_par = 90
elif hill_type == 'large':
    hill_height = 70
    hill_points = 1.8
    hill_par = 120

