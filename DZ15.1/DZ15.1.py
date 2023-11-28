number = int(input("Please enter your number >0 and <8640000:"))
end_dict = {'1':'день', '2':'дні', '3':'дні', '4':'дні', '5':'днів', '6':'днів', '7':'днів', '8':'днів', '9':'днів', '0':'днів'}
days_number = str(number // 86400)
hours = str(number % 86400 // 60 // 60)
minutes = str(number % 86400 // 60 % 60)
sec = str(number % 86400 % 60)
last_digit = days_number[len(days_number)-1]
print(f'{days_number} {end_dict[last_digit]}, {hours.zfill(2)}:{minutes.zfill(2)}:{sec.zfill(2)}')
