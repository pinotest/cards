from faker import Faker
from datetime import datetime
from BaseContact import BaseContact
from BusinessContact import BusinessContact

fake = Faker('pl_PL')

def create_contacts(card_type, amount):
    '''
    Function gets two arguments: 
    card type 0 - create businessContact or other - create BaseContact
    amount - number of cards to create
    and return a list of created cards
    '''
    if card_type == 0:
        return [BusinessContact(fake.company(), fake.job(), fake.phone_number(),fake.first_name(),fake.last_name(), 
        fake.phone_number(), fake.email()) for i in range(amount)]
    return [BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()) for i in range(amount)]
cards = create_contacts(0,10) 
print(cards)
print(cards[0].contact())
