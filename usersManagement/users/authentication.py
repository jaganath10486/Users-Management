from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
import firebase_admin
from firebase_admin import credentials, auth
from rest_framework.exceptions import AuthenticationFailed


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')
        id_token = id_token.split(" ").pop()
        print("Id Token : ", id_token)
        if not id_token:
            return None  
        try:
            decoded_token = auth.verify_id_token(id_token)
            print(decoded_token)
            user = auth.get_user(decoded_token['uid'])
            print("user : ", user)
            return (user, None)
        except Exception as e:
            raise AuthenticationFailed(str(e))