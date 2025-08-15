from django.urls import path
from home.views import test, user_home, user_profile, landing, index, test_layout, test_layout_content

# best practice is to create urls file in each app folder
urlpatterns = [
    path('test', test, name='testpage'),
    path('land', landing, name='landing'),
    path('index', index, name='index'),
    path('test_layout', test_layout, name='test_layout'),
    path('tst', test_layout_content, name='test_layout_content'),
    path('<name>', user_home, name='user_home'),
    # path('profile/<id>', user_profile, name='user_profile'),
    path('profile/<int:id>', user_profile, name='user_profile') ,# limit the id to be an integer only
   
]
