from django.urls import path, include

from accounts.views import profile, CreateAccountView


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
    path('register/', CreateAccountView.as_view(), name='register'),
]