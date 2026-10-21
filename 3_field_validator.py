from pydantic import BaseModel, field_validator, EmailStr

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode= 'before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            return ValueError('Age should be in between 0 and 100')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

patient_info = {'name':'Ashutosh',
                'age':21,
                'email':'ashu@hdfc.com'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)