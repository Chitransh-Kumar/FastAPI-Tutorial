from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    # allergies: List[str]
    contact_details: Dict[str, str] 

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains= ['hdfc.com', 'icici.com']

        domain_name= value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    
patient_info= {
    'name': 'Chitransh',
    'email': 'abc@gmail.com',
    'age': 22,
    'weight': 83.5,
    'married': False,
    'contact_details': {
        'phone': '8031980413'
    }
}

patient1= Patient(**patient_info)

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.married)

    print("Inserted")

insert_patient_data(patient1)