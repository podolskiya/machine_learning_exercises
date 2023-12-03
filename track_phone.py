import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse('number')
print(geocoder.description _for_numer(phone_number, 'en'))

# if number: +44**********, prints 'Russia'
