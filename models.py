from pydantic import BaseModel
#import datetime

class Student(BaseModel):
    id: int
    ime: str
    Fakultet: str
    godinaStudija: int
#    godinaRodjenja: datetime
    Budzet: bool
    
    
    
    
