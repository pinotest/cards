from faker import Faker
from datetime import datetime
from BaseContact import BaseContact
from BusinessContact import BusinessContact

fake = Faker('pl_PL')

def give_time(func):
    start = datetime.now()
    def wrapper(*args, **kwargs):
        return duration
    duration = datetime.now() - start
    print(duration)
    return wrapper      

@give_time
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
# for i in range(5):
#     ob = "ob"+str(i)
#     ob = NewPostcard(fake.first_name() ,fake.last_name(), fake.company(), fake.job(), fake.email());
    #print(ob.name, ob.lastname, ob.company, ob.position, ob.mail);
    #print(ob)

# card_one = BaseContact(fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
# card_two = BusinessContact(fake.company(), fake.job(), fake.phone_number(),fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
# card_three = BaseContact(fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
#cards = [card_one, card_two, card_three]

# by_name = sorted(cards, key=lambda card: card.name)
# by_lastname = sorted(cards, key=lambda card: card.lastname)
# by_mail = sorted(cards, key=lambda card: card.mail)
# print(cards)
# print(by_name[0]);
# print(by_lastname[0]);    
# print(by_mail[0]);    
cards = create_contacts(0,3000) 
# print(cards)
# for i,j in enumerate(cards):
#     print(cards[i].contact())