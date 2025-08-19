print('🚀 Welcome to name-art-generator')
name = input("Enter your name: ")
decoration = input("Pick a decoration character (e.g., * ~ #): ")

border = decoration * (len(name) + 6)
print("\n" + border)
print(f"{decoration*2} {name.upper()} {decoration*2}")
print(border)
