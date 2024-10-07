# Programmed by John Elehwany and Krishon Pinkins
# Loyola CS151, Professor Zee
# Due Date: October 2, 2024
# Lab Assignment: 03

# This project calculates the points gained from a ski jump depending on the speed, time in air, and other factors.

# Imports math to program
import math

print("""
Ski Jump Calculator
""")

# DATA IN

# Asks for input of hill type. The chosen hill type then changes the values of the height, PPM, and par.
hill_type = input("Enter hill type (normal or large): ")
if hill_type == "normal":
        hill_height = 46
        hill_ppm = 2
        hill_par = 90
elif hill_type == "large":
        hill_height = 70
        hill_ppm = 1.8
        hill_par = 120
else:
        print("Invalid hill type. Please input again.")

# Asks for input of the speed of jumper.
speed = float(input("Enter speed of the jumper: "))

# PROCESSING

# Calculates the time spent in the air using the imported math module.
air_time = math.sqrt((2 * hill_height) / 9.8)
# Calculates the distance travelled.
distance = air_time * speed

# Calculates the points earned.
points_earned = 60 + (distance - hill_par) * hill_ppm

# OUTPUT

# Determines output depending on what the points earned is.
if points_earned > 61:
    print("Great job for doing better than par!")
elif points_earned <= 10:
    print("What happened?")
else:
    print("Sorry you didn't go very far.")

# Outputs the user's distance and total points.
print("""
You had a total distance of""", distance, "and a total score of", points_earned)