from pydantic import BaseModel

class PostRequest(BaseModel):
    business:str
    tone:str
    promotion:str


