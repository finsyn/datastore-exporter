import http.client, urllib.parse
from os import environ
import json
from auth import credentials
from google.auth.transport.requests import AuthorizedSession

keyfile = environ['GCP_KEYFILE']
project_id = environ['GCP_PROJECT']
bucket = environ['GCP_BUCKET']

credentials = credentials(keyfile)
authed_session = AuthorizedSession(credentials)

payload = json.dumps({
    'outputUrlPrefix': 'gs://%s' % bucket,
    'entityFilter': {
        'kinds': ['shares'],
        'namespaceIds': ['default']
    }
  })

response = authed_session.post(
    'https://datastore.googleapis.com/v1/projects/%s:export' % project_id,
    data = payload
)

print(response.text)
