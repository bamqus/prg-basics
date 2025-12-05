
with open("pets.txt", "r") as file:
    total_words = 0

    for line in file:
        print(line, end="")               
        words = line.split()             
        total_words += len(words)         

print("Total number of words:", total_words)