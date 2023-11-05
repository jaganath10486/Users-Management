from rest_framework import generics, viewsets, status, response
from rest_framework.authentication import BaseAuthentication
from rest_framework import permissions
import firebase_admin
from firebase_admin import credentials, auth

from django.conf import settings
from .firestore_user import UserManagement
from .serializers  import RegisterSerializer, LoginSerializer
from .authentication import FirebaseAuthentication

class RegisteUser(viewsets.ViewSet):
    user = UserManagement()

    def create(self, request):
        serializer = RegisterSerializer(request.data)

        print(serializer.data)
        try:
            user = auth.create_user(email = serializer.data['email'], password = serializer.data['password'])
            # print("User : ", user['uid'])
            auth.generate_email_verification_link(user.email)
            self.user.register(serializer.data, user.uid)
            return response.Response({"data" : serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error in storing", e)
            return response.Response({"data" : e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LoginView(viewsets.ViewSet):

    def create(self, request):
        serializer = LoginSerializer(request.data)
        try:
            user = auth.get_user_by_email(serializer.data['email'])
            print("email exists : ", user)
        except auth.UserNotFoundError as e:
            return response.Response({"message" : 'Email Not Found'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            print("emil updated")
            token = auth.create_custom_token(user.uid)
            print(token)
            return response.Response({"Token" : token})
        except auth.UserNotFoundError as e:
            print(e)
            return response.Response({"message" : 'User Not Found'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
class ProfileView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (FirebaseAuthentication,)
    def list(self, request):
        return response.Response({"message" : "Authenticated"}, status=status.HTTP_200_OK)
    def update(self, request):
        pass
    def delete(self, request):
        pass
        
