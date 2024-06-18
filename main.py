# main.py
from fastapi import FastAPI, Header, HTTPException, Body, Query
import requests
import os
import dotenv
import logging
import schema

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPES = os.getenv("SCOPES")
STATE = os.getenv("STATE") # For CSRF reasons

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

app = FastAPI()

@app.get('/callback')
async def callback(code: str = Query()):
    if code:
        try:
            access_token = exchange_code_for_token(code)
            return {'access_token': access_token}
        except Exception as e:
            logging.error(f"Token exchange failed: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    raise HTTPException(status_code=400, detail="No access token found")

@app.get("/linkedin/userinfo")
async def get_linkedin_user_info():
    user_info_url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(user_info_url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch user info")
    return response.json()

@app.post("/linkedin/post")
async def create_linkedin_post(post: schema.TextPost = Body()):

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    payload = {
        "author": f"urn:li:person:{post.author_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post.caption
                },
                "shareMediaCategory": post.mediaType
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": post.visibility
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return {"code": response.status_code}



def exchange_code_for_token(code: str):
    token_url = f"https://www.linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code={code}&redirect_uri={REDIRECT_URI}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&state={STATE}"
    response = requests.get(token_url)
    print(response.url)

    if response.status_code != 200:
        print(response.text)
        raise HTTPException(status_code=400, detail="Failed to obtain access token")
    access_token = response.json().get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="No access token found")
    print(access_token)
    return access_token