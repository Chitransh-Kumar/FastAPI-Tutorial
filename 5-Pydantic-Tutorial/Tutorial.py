from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str= Field(max_length= 50) # Max length of name should be 50
    email: EmailStr
    age: Annotated[int, Field(gt= 0, lt= 80, title= "Age of the patient", description= "Age of the patient should be greater than 0 and less than 80", examples= [20, 25], default= 35)]
    weight: float= Field(gt= 0, lt= 100) # Weight should be greater than 0
    married: Optional[bool]= None # If a field is Optional it should have default value None
    allergies: Optional[List[str]]= Field(max_length= 5)
    contact_details: Dict[str, str] # key(data-type)-value(data-type)

patient_info= {
    'name': 'Chitransh',
    'email': 'abc@gmail.com',
    'age': 22,
    'weight': 83.5,
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

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)

    print("Updated")

insert_patient_data(patient1)