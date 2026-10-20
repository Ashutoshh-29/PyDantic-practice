from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

def user_data(user : User):
    print(user.name)
    print(user.age)

user_info = {'name': 'Ashutosh', 'age': '18'}

user1 = User(**user_info)

user_data(user1)