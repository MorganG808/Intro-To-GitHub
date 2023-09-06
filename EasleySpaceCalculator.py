print("Welcome to the Space Traveler Calculator!")

distance = int(input("Enter the distance of the celestial object in lightyears: "))
speed = int(input("Enter the spacecraft speed in lightyears: "))

time = distance/speed
print("It will take " + str(time) + " lightyears (?) to reach your destination!")
