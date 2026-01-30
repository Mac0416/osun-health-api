from fastapi import FastAPI
from pydantic import BaseModel
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Osun Health API"}

class TokenRequest(BaseModel):
    room_name: str
    identity: str

@app.post("/video/token")
def generate_video_token(req: TokenRequest):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    api_key = os.environ.get("TWILIO_API_KEY_SID")
    api_secret = os.environ.get("TWILIO_API_KEY_SECRET")
    token = AccessToken(account_sid, api_key, api_secret, identity=req.identity)
    video_grant = VideoGrant(room=req.room_name)
    token.add_grant(video_grant)
    jwt_token = token.to_jwt().decode("utf-8") if hasattr(token.to_jwt(), "decode") else token.to_jwt()
    return {"token": jwt_token}

@app.get("/chat/qa")
def get_qa():
    return {
        "qa": [
            {"question": "What is blood pressure?", "answer": "Blood pressure is the force of blood pushing against your artery walls."},
            {"question": "How often should I measure my glucose?", "answer": "Follow your doctor's guidance, typically before meals and at bedtime."}
        ]
    }
