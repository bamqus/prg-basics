car_number = input('Enter car registration number: ')
is_krakow = car_number.upper().startswith(('KR', 'KK'))
print(f'Car is from Krakow: {is_krakow}')