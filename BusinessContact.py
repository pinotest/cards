from BaseContact import BaseContact

class BusinessContact(BaseContact):
    def __init__(self, company, position, business_mobile,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_mobile = business_mobile
    def contact(self):
       print(f"Wybieram numer {self.business_mobile} i dzwonię do {self.name} {self.lastname}")
