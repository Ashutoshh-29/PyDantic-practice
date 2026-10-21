from pydantic import BaseModel, computed_field

class User(BaseModel):
    name : str
    age : int
    weight : float #In Kg
    height : float #In metre

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def insert_user_data(user: User):
    print(user.name)
    print(user.age)
    print(user.weight)
    print(user.height)
    print('BMI', user.bmi)

user_info = {'name': 'Ashutosh',
                'age': '21',
                'weight': 50.5,
                'height': 1.65}

user1 = User(**user_info)

insert_user_data(user1)