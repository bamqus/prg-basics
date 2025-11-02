university = "Krakow University of Economics"
parts = university.split()
abbrev = ''.join(p[0] for p in parts)
print(abbrev)