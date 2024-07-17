from fastapi import FastAPI
from pydantic import BaseModel

class SubPage(BaseModel):
    heading : str | None = "Subpage Heading"
    description : str | None = "Description of Subpage"
    footer : str | None = "Footer of Subpage"
    page_no : int = 0
    page_dim : float = 0.0

app = FastAPI()

@app.post('/sub')
async def subPage(sub:SubPage):
    return sub.page_no * sub.page_dim