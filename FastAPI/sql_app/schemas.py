from pydantic import BaseModel

# To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models.

class SubPageBase(BaseModel):
    heading : str
    description : str
    footer : int
    page_no : int
    page_dim : float

class SubPageCreate(SubPageBase):
    pass

class SubPage(SubPageBase):
    id : int
    class Config:
        orm_mode = True
        