from faker import Faker

fake = Faker('pl_PL');

class NewPostcard:

    def __init__(self, name, lastname, company, position, mail):
        self.name = name;
        self.lastname = lastname;
        self.company = company;
        self.position = position;
        self.mail = mail;

        self._name_long = 0;    
    def __str__(self):
        return f'{self.name} {self.lastname} {self.mail}'
    def __repr__(self):
        return f"Card(name={self.name} lastname={self.lastname}, company={self.company}, position={self.position}, mail={self.mail})"
    def __eq__(self, other):
        return all (
            (self.name == other.name,
            self.lastname == other.lastname,
            self.company == other.company,
            self.position == other.position,
            self.mail == other.mail
            
            )

        )
    # def __gt__(self, other):
    #         return self.name > other.name
    def contact(self):
       print(f"Kontaktuje się z {self.name} {self.lastname} {self.position} {self.company}")

    @property
    def name_long(self):
        return ((str(len(self.name)) +" "+str(len(self.lastname))))

for i in range(5):
    ob = "ob"+str(i)
    ob = NewPostcard(fake.first_name() ,fake.last_name(), fake.company(), fake.job(), fake.email());
    #print(ob.name, ob.lastname, ob.company, ob.position, ob.mail);
    #print(ob)

card_one = NewPostcard(fake.first_name() ,fake.last_name(), fake.company(), fake.job(), fake.email());
card_two = NewPostcard(fake.first_name() ,fake.last_name(), fake.company(), fake.job(), fake.email());
card_three = NewPostcard(fake.first_name() ,fake.last_name(), fake.company(), fake.job(), fake.email());
cards = [card_one, card_two, card_three]

by_name = sorted(cards, key=lambda card: card.name)
by_lastname = sorted(cards, key=lambda card: card.lastname)
by_mail = sorted(cards, key=lambda card: card.mail)
# print(cards)
# print(by_name[0]);
# print(by_lastname[0]);    
# print(by_mail[0]);    
print(card_one.name_long)