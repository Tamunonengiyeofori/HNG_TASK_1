from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def root():
    return {"message": "WELCOME TO MY HNG TASK 1"}
    


@app.get("/user_info")
def get_details():
    return details
    