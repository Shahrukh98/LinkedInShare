import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

def generate_auth_url():
    """Generate and return the OAuth2 authorization URL for LinkedIn."""

    base_url = "https://www.linkedin.com/oauth/v2/authorization"
    client_id = os.getenv("LINKEDIN_CLIENT_ID")
    redirect_uri = os.getenv("LINKEDIN_REDIRECT_URI")
    ## Since we might have multiple scopes with spaces between, so we need to convert scope
    scope = quote(os.getenv("LINKEDIN_SCOPES")) 
    state = os.getenv("LINKEDIN_STATE")
    response_type = "code"

    url = f"{base_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}&response_type={response_type}"
    return url

if __name__ == "__main__":
    print("Navigate to this URL in your web browser to authorize: ")
    print(generate_auth_url())