import facebook
import urllib.request
import urllib.parse
import urllib.error
import sys

def get_app_access_token(app_id, app_secret):
    args = {
        'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret
    }

    data = urllib.parse.urlencode(args).encode()

    try:
        with urllib.request.urlopen("https://graph.facebook.com/oauth/access_token", data) as response:
            result = str(response.read()).replace('\'','').split('=')[1]
            return result
    except urllib.error.URLError as error:
        print(error)
        sys.exit(2)

user = 'heckfy.i'
app_id = '201916420249251'
app_secret = '3ee1663f80599d64ad5b848d4ad68485'

access_token = get_app_access_token(app_id, app_secret)

graph = facebook.GraphAPI(access_token)
profile = graph.get_object("me")
posts = graph.get_connections(profile['id'], 'posts')

email = profile['email'] # Get email
name = profile['name'] # Get name