from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Osun Health API"}

# TODO: Add endpoints for appointments, vitals, meds, and more.
