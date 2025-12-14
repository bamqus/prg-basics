

seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]


file_name = 'seven_wonders.txt'

seven_wonders_sorted = sorted(seven_wonders)

with open(file_name, 'w') as f:
    for item in seven_wonders_sorted:
        f.write(item + "\n")


with open(file_name, 'r') as f:
    print(f.read())




