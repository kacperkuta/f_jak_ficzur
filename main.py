from fastapi import FastAPI, HTTPException
app = FastAPI()

from pydantic import BaseModel

@app.get("/")
def root():
	return {"message": "Hello World during the coronavirus pandemic!"}


@app.get("/welcome")
def welcome_to_the_jungle():
	return {"message": "Welcome to the jungle! We have funny games!"}

