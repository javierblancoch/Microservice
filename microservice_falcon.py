import falcon
from uuid import uuid4

#generating token
rand_token = uuid4()
print(rand_token)

class AuthMiddleware(object):
    def process_request(self, req, resp):
        token = req.get_header('Authorization')
        challenges = ['Token type="Fernet"']

        if token is None:
            description = ('Please provide an auth token as part of the request.')

            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

        if not self._token_is_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')

            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

    def _token_is_valid(self, token):
        if token==str(rand_token):
            return True
        else:
            return False

class Resource:
    def on_get(self, req, resp):
        content = {
            'content': (
                "The content of your microservice."
            ),
            'author': 'javierblancoch'
        }
        resp.media = content

api = falcon.API(middleware=[
    AuthMiddleware(),
])
api.add_route('/api', Resource())