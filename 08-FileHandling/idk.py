# open("example.txt", "r") do odczutu
# open("example.txt", "w") do zapisu
# open("example.txt", "a") dopisywanie do pliku

file = open("example.txt", "r")
content = file.read() 

file.close()

print(content)




###########################

with open('example.txt','r') as file: 
    content = file.read()

print(content)

