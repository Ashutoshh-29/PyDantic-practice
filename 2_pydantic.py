from pydantic import BaseModel, EmailStr , AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length= 50, title = 'name of the patient', description= 'give the name of patients in less than 50 chars', example= ['Ashu','Ashutosh'])]
    age : int = Field(gt = 0, lt= 120)
    weight: Annotated[float, Field(gt=0,strict = True)]
    married: Annotated[bool, Field(default = False, description='Patient is married or not')]
    allergies: Annotated[Optional[List[str]],Field(default = None, max_length= 10)]
    email: EmailStr
    linkdin: AnyUrl
    contact_details: Dict[str , str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.linkdin)
    print(patient.contact_details)

patient_info = {'name': 'Ashutosh',
                'age': '21',
                'weight': 50.5,
                'email': 'abc@gmail.com',
                'linkdin': 'http://linkdin.com//1322',
                'contact_details':{'phone_no':'123456'}
                }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

