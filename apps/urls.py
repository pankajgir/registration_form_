from django.urls import path
from .views import home, Signup

urlpatterns = [
    path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
]