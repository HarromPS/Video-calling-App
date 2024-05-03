
# import path module from urls of django module
from django.urls import path

# from current directory import the view file
from home import views

# URL configuration module -> it should be configured in main url file of the project 
# create a variable name urlpatterns-> to store url pattern objects
urlpatterns = [ 
    # all request of playground is handled by this url 
    # i.e localhost:8000/hello can be used instead of localhost:8000/playground/hello
    path('',views.index,name='home'),
    path('index/',views.index,name='index'),
    path('signup/',views.signUpUser,name='signUpUser'),
    path('login/',views.loginUser,name='loginUser'),
    path('logout/',views.logoutUser,name='logoutUser'),
    path('meeting/',views.videoCall,name='meeting'),
    path('join_meet/',views.joinRoom,name='join_meet'),
]