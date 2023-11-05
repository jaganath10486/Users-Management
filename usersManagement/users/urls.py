from django.urls import path
from .views import RegisteUser, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisteUser.as_view({'post': 'create'}), name='Register Endpoint'),
    path('login/', LoginView.as_view({'post' : 'create'}), name='Login Endpoint'),
    path('profile/', ProfileView.as_view({'get' : 'list', 'put' : 'update', 'delete' : 'delete'}), name='Profile View')
]
