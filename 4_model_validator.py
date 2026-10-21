from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    allergies : List[str]
    contact_detail : Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_detail)

patient_info = {'name':'Ashutosh', 
                 'age': '65',
                 'email':'abc@icici.com',
                 'allergies': ['pollen', 'dust'], 
                 'contact_detail':{'phone':'2353462', 
                                    'emergency':'235236'}
                                    }

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)