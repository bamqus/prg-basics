with open('countries.txt', 'r') as file:
    n = 1
    for line in file:
        print(f"{n}. {line}", end="")
        n += 1