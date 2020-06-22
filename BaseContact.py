
class BaseContact:

    def __init__(self, name, lastname, mobile, mail):
        self.name = name
        self.lastname = lastname
        self.mobile = mobile
        self.mail = mail

        self._label_length = 0
            
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