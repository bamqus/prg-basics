countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Jamaica", "population": 1000000},
    {"name": "Argentina", "population": 5000000},
    {"name": "France", "population": 2500000},
    {"name": "Italy", "population": 40000},
]

for country in countries:
    print(f"{country['name']:8} {country['population']}")