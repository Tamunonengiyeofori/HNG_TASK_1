from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


details = {
    "slackUsername": "Nengi_Tammy",
    "backend": True,
    "age": 21,
    "bio": " I am an aspiring python developer who works with FatsAPI and Django"
    
}


# class UserInfo(BaseModel):
#     slackUsername : str
#     backend : bool
#     age: int
#     bio : str   




@app.get("/")
def get_details():
    return details
    