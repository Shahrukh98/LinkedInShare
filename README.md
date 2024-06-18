# LinkedIn API Project

This application interfaces with LinkedIn's sharing platform to create UGC (User Generated Content) posts. It provides functionality to authenticate with LinkedIn, exchange authorization codes for tokens, and create posts on LinkedIn of different type i.e. plain text, articles, images or videos.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package installer)


### Installation


1. **Clone the Repository**
   Clone the repository using the following command:
   ```bash
   git clone https://github.com/Shahrukh98/LinkedInShare.git
   cd LinkedInShare
   ```

2. **Set Up a Virtual Environment**
Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate
   ```
   
3. **Install Required Packages**
Install all required packages that are used in the project:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Environment Variables**
   Set up the necessary environment variables by creating a `.env` file in the root directory of your project. Populate it with the following entries (can also be found in `.env.example`):

   ```plaintext
    CLIENT_ID=your_client_id # paste your own
    CLIENT_SECRET=your_client_secret # paste your own
    REDIRECT_URI=http://localhost:8000/callback # or paste your own if you have one setup
    SCOPES=your_scope1 your_scope2 ...other_scopes # write all scopes with seperated by space like: profile email ...other scopes
    STATE=your_state # to prevent csrf attacks
    ACCESS_TOKEN=your_access_token # Obtain this after authentication
2. **OAuth App Setup**
   
If you already have a Linkedin developer application:

    Replace the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI values in your .env file with those from your existing app. Make sure you know the SCOPE of your app and add them on the app and .env.

If you need to set up a new LinkedIn developer application:

    Register a new app on the LinkedIn developer platform and use the redirect URL provided in .env.example.
    Make sure to copy your CLIENT_ID, CLIENT_SECRET, REDIRECT_URI and SCOPE to the .env file.


 Note: The STATE parameter in OAuth 2.0 and OpenID Connect (OIDC) authorization requests is a critical component for protecting against Cross-Site Request Forgery (CSRF) attacks and maintaining the integrity of the authorization flow. Make sure to add the STATE variable in .env to make the app less susceptible to CSRF attacks.

### Setting up


1. **Start the Flask Server**
Start the server by running the following command:
   ```bash
   uvicorn main:app --port=[YOUR_PORT]
   ```
2. **Generate Authentication URL**
To authenticate with LinkedIn app and obtain your token, run the following script to generate an authorization URL:

   ```bash
   python generate_auth_url.py 
   ```


3. **Follow the URL Generated in Step 2, then authorize the app**
it shall then exchange the code with access token, and redirects you to the specified redirect URI, where you will be able to access the token. Put the access token in the .env and restart the app.

### Using Endpoints
After retreiving the access token and placing it in .env. You can retrieve user info from the `/linkedin/userinfo`. Then using the id of user and following different post schemas, you can use `/linkedin/post` to create post on the respective user feed.
