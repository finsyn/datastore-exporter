from google.auth import crypt
from google.auth import jwt
from google.oauth2 import service_account

def credentials(keyfile):
    scopes = ['https://www.googleapis.com/auth/datastore']
    credentials = service_account.Credentials.from_service_account_file(
        keyfile,
        scopes=scopes
    )
    return credentials
