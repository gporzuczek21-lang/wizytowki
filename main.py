from faker import Faker
fake= Faker('pl_PL')

typee = input("podaj rodzaj wizytwki poslugujac sie odpowiednia cyfrom 1.BaseContact 2.BusinessContact:" )
how_many = int(input("Podaj ilosc wizytowek: "))
base = []
buis = []

class BaseContact:
    def __init__(self, name, last_name, number, email):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.email = email
    
    @property
    def label(self):
        self._label = len(self.name) +len(self.last_name)
        return f"Suma znaków w imieniu i nazwisku to: {self._label}" 
    
    def __str__(self):
        return f"Wizytówka: {self.name} {self.last_name} {self.email}\n"
    
    def __contact__(self):
        return f"Wybieram numer +48 {self.number} i dzwonie do {self.name} {self.last_name}\n"  

    def __repr__ (self):
        return f"BaseContact(first_name = {self.name} last_name = {self.last_name} number = {self.number}, email = {self.email})\n" 

class BusinessContact(BaseContact):
    def __init__(self, job, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_phone = work_phone 
    @property
    def label(self):
        self._label = len(self.name) +len(self.last_name)
        return f"Suma znaków w imieniu i nazwisku to: {self._label}" 
     
    def __contakt__(self):
        return f"Wybieram numer +48 {self.work_phone} i dzwonie do {self.name} {self.last_name}\n" 
    def __repr__ (self):
        return f"BusinessContact(first_name = {self.name}, last_name = {self.last_name}, number = {self.number}, email = {self.email}, job = {self.job}, company= {self.company} work_phone={self.work_phone})\n"

def create_contacts(typee, how_many):
    for i in range(0, how_many):
        if typee == '1':
            i = BaseContact(name=fake.first_name(), last_name=fake.last_name(), number=fake.phone_number(), email=fake.email())
            base.append(i)
            print(i.__contact__())
            print(i)
            print(i.__repr__())
            print(i.label)
        elif typee == '2':
            i = BusinessContact(name=fake.first_name(), last_name=fake.last_name(), number=fake.phone_number(), email=fake.email(),job=fake.job(), company=fake.company(),work_phone=fake.phone_number())        
            buis.append(i)
            print(i.__contact__())
            print(i)
            print(i.label)
        else:
            print("Nieprawidłowy wybór")        

if __name__=="__main__":    
    create_contacts(typee, how_many)       
    print(base)
    print(buis)