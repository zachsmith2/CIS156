#Zachary Smith
#PA_2

richter = (float(input("Please enter the richter scale value for the earthquake:  ")))
description="" #define description which will later be added in place of "effect"

if richter>=8.0:#Richter scale for earthquakes larger than 8
    description="Most structures fail"
elif richter>=7.0:#Richter scale for earthquakes larger than 7
    description="Many buildings destroyed"
elif richter>=6.0:#Richter scale for earthquakes larger than 6
    description= "Many buildings considerably damaged, some collapse"
elif richter>=4.5:#Richter scale for earthquakes larger than 4.5
    description= "Damage to poorly constructed buildings"
elif richter<4.5:#Richter scale for earthquakes less than 4.5
    description= "No destruction of buildings"
else:
    print("Error")

print(description)