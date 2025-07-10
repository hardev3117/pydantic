from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    phone: str= Field(min_length=10, max_length=10, description="phone number should be 10 number")
    linkedin_url: Annotated[AnyUrl, Field(description="linkedin_url should be valid url")]
    age: int = Field(gt=0, lt=90, description="age field for entering age , age should be between 0 t0 120 years")
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.linkedin_url)
    print(patient.phone)
    print('updated')

patient_info = {'name':'nitish', 'phone':'9887888882', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '89', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)