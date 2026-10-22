from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str 
    age: int
    address: Address

address_dict = {'city': 'Varanasi', 'state': 'Uttar Pradesh', 'pin': '221001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Ashu','gender':'Male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

#temp = patient1.model_dump(include= ['name','age'])
temp1 = patient1.model_dump(exclude = {'address': ['pin']})

print(temp1)
print(type(temp1))

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))