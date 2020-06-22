from faker import Faker

fake = Faker('pl_PL');

class BaseContact:

    def __init__(self, name, lastname, mobile, mail):
        self.name = name;
        self.lastname = lastname;
        self.mobile = mobile;
        self.mail = mail;

        self._label_length = 0;    
    def __str__(self):
        return f'{self.name} {self.lastname} {self.mail}'
    def __repr__(self):
        return f"Card(name={self.name} lastname={self.lastname}, phone={self.mobile}, mail={self.mail})"
    def __eq__(self, other):
        return all (
            (self.name == other.name,
            self.lastname == other.lastname,
            self.mobile == other.mobile,
            self.mail == other.mail
            
            )

        )
    # def __gt__(self, other):
    #         return self.name > other.name
    def contact(self):
       print(f"Wybieram numer {self.mobile} i dzwonię do {self.name} {self.lastname}")

    @property
    def label_length(self):
        return ((str(len(self.name)) +" "+str(len(self.lastname))))

class BusinessContact(BaseContact):
    def __init__(self, company, position, business_mobile,*args, **kwargs):
        super().__init__(*args, **kwargs);
        self.company = company;
        self.position = position;
        self.business_mobile = business_mobile;
    def contact(self):
       print(f"Wybieram numer {self.business_mobile} i dzwonię do {self.name} {self.lastname}")

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

card_one = BaseContact(fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
card_two = BusinessContact(fake.company(), fake.job(), fake.phone_number(),fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
card_three = BaseContact(fake.first_name() ,fake.last_name(), fake.phone_number(), fake.email());
cards = [card_one, card_two, card_three]

# by_name = sorted(cards, key=lambda card: card.name)
# by_lastname = sorted(cards, key=lambda card: card.lastname)
# by_mail = sorted(cards, key=lambda card: card.mail)
# print(cards)
# print(by_name[0]);
# print(by_lastname[0]);    
# print(by_mail[0]);    
cards = create_contacts(2,10) 
print(cards)
for i,j in enumerate(cards):
    print(cards[i].contact())

