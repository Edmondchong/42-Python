from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)

Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")

print(Joffrey.eyes)  # Use 'eyes' to get the eye color
print(Joffrey.hairs)  # Use 'hairs' to get the hair color

print(Joffrey.__dict__)
