from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : int

class User(BaseModel):
    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city':'Varanasi',
                'state': 'Uttar Pradesh',
                'pincode': 221001}

address1 = Address(**address_dict)

user_dict = {'name': 'Ashutosh',
             'gender': 'Male',
             'age': 21,
             'address': address1}

user1 = User(**user_dict)

print(user1)
print(user1.address.city)
print(user1.address.pincode)